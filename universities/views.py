"""
AusUni Views
All views for the Australian University Portal
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count, Avg
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib import messages
from .models import State, City, University, Campus, Course, Scholarship, Bookmark


# ─── HOME ────────────────────────────────────────────────────────────────────

def home(request):
    states = State.objects.annotate(uni_count=Count('universities')).order_by('name')
    featured_unis = University.objects.filter(is_featured=True).select_related('state', 'city')[:6]
    popular_courses = Course.objects.filter(is_popular=True).select_related('university')[:8]
    total_universities = University.objects.count()
    total_courses = Course.objects.count()
    total_scholarships = Scholarship.objects.count()

    context = {
        'states': states,
        'featured_unis': featured_unis,
        'popular_courses': popular_courses,
        'total_universities': total_universities,
        'total_courses': total_courses,
        'total_scholarships': total_scholarships,
    }
    return render(request, 'universities/home.html', context)


# ─── STATE ───────────────────────────────────────────────────────────────────

def state_detail(request, slug):
    state = get_object_or_404(State, slug=slug)
    cities = state.cities.annotate(uni_count=Count('universities')).order_by('name')
    universities = University.objects.filter(state=state).select_related('city').annotate(
        course_count=Count('courses'),
        scholarship_count=Count('scholarships'),
    ).order_by('name')

    type_filter = request.GET.get('type')
    if type_filter:
        universities = universities.filter(institution_type=type_filter)

    context = {
        'state': state,
        'cities': cities,
        'universities': universities,
        'type_filter': type_filter,
    }
    return render(request, 'universities/state_detail.html', context)


# ─── CITY ────────────────────────────────────────────────────────────────────

def city_detail(request, state_slug, city_slug):
    state = get_object_or_404(State, slug=state_slug)
    city = get_object_or_404(City, slug=city_slug, state=state)
    universities = University.objects.filter(city=city).select_related('state').annotate(
        course_count=Count('courses'),
        scholarship_count=Count('scholarships'),
    ).order_by('name')

    context = {
        'state': state,
        'city': city,
        'universities': universities,
    }
    return render(request, 'universities/city_detail.html', context)


# ─── UNIVERSITY LIST ─────────────────────────────────────────────────────────

def university_list(request):
    universities = University.objects.select_related('state', 'city').annotate(
        course_count=Count('courses'),
        scholarship_count=Count('scholarships'),
    )

    # Filters
    state_filter = request.GET.get('state')
    type_filter = request.GET.get('type')
    group_filter = request.GET.get('group')
    search_q = request.GET.get('q', '').strip()

    if state_filter:
        universities = universities.filter(state__slug=state_filter)
    if type_filter:
        universities = universities.filter(institution_type=type_filter)
    if group_filter:
        universities = universities.filter(group_affiliation=group_filter)
    if search_q:
        universities = universities.filter(
            Q(name__icontains=search_q) |
            Q(city__name__icontains=search_q) |
            Q(description__icontains=search_q)
        )

    universities = universities.order_by('name')
    paginator = Paginator(universities, 12)
    page = request.GET.get('page')
    universities_page = paginator.get_page(page)

    states = State.objects.annotate(uni_count=Count('universities')).order_by('name')

    context = {
        'universities': universities_page,
        'states': states,
        'state_filter': state_filter,
        'type_filter': type_filter,
        'group_filter': group_filter,
        'search_q': search_q,
        'total_results': paginator.count,
    }
    return render(request, 'universities/university_list.html', context)


# ─── UNIVERSITY DETAIL ───────────────────────────────────────────────────────

def university_detail(request, slug):
    university = get_object_or_404(
        University.objects.select_related('state', 'city'),
        slug=slug
    )
    campuses = university.campuses.select_related('city', 'state').order_by('-is_main')
    courses = university.courses.order_by('level', 'name')
    scholarships = university.scholarships.order_by('-coverage_percentage', 'name')

    # Parse popular courses into a list
    popular_courses_list = []
    if university.popular_courses:
        popular_courses_list = [c.strip() for c in university.popular_courses.split(',')]

    # Group courses by level
    course_levels = {}
    for course in courses:
        level = course.get_level_display()
        if level not in course_levels:
            course_levels[level] = []
        course_levels[level].append(course)

    # Bookmark check
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    is_bookmarked = Bookmark.objects.filter(
        session_key=session_key, university=university
    ).exists()

    context = {
        'university': university,
        'campuses': campuses,
        'courses': courses,
        'course_levels': course_levels,
        'scholarships': scholarships,
        'is_bookmarked': is_bookmarked,
        'popular_courses_list': popular_courses_list,
    }
    return render(request, 'universities/university_detail.html', context)


# ─── COURSE LIST ─────────────────────────────────────────────────────────────

def course_list(request):
    courses = Course.objects.select_related('university', 'university__state', 'university__city')

    # Filters
    state_filter = request.GET.get('state')
    level_filter = request.GET.get('level')
    field_filter = request.GET.get('field')
    max_fee = request.GET.get('max_fee')
    ielts_max = request.GET.get('ielts_max')
    search_q = request.GET.get('q', '').strip()

    if state_filter:
        courses = courses.filter(university__state__slug=state_filter)
    if level_filter:
        courses = courses.filter(level=level_filter)
    if field_filter:
        courses = courses.filter(field_of_study__icontains=field_filter)
    if max_fee:
        try:
            courses = courses.filter(tuition_fee_annual__lte=float(max_fee))
        except ValueError:
            pass
    if ielts_max:
        try:
            courses = courses.filter(ielts_overall__lte=float(ielts_max))
        except ValueError:
            pass
    if search_q:
        courses = courses.filter(
            Q(name__icontains=search_q) |
            Q(field_of_study__icontains=search_q) |
            Q(university__name__icontains=search_q)
        )

    courses = courses.order_by('tuition_fee_annual', 'name')
    paginator = Paginator(courses, 12)
    page = request.GET.get('page')
    courses_page = paginator.get_page(page)

    states = State.objects.order_by('name')
    level_choices = Course.LEVEL_CHOICES

    context = {
        'courses': courses_page,
        'states': states,
        'level_choices': level_choices,
        'state_filter': state_filter,
        'level_filter': level_filter,
        'field_filter': field_filter,
        'max_fee': max_fee,
        'ielts_max': ielts_max,
        'search_q': search_q,
        'total_results': paginator.count,
    }
    return render(request, 'universities/course_list.html', context)


# ─── COURSE DETAIL ───────────────────────────────────────────────────────────

def course_detail(request, uni_slug, course_slug):
    university = get_object_or_404(University, slug=uni_slug)
    course = get_object_or_404(Course, slug=course_slug, university=university)
    related_courses = Course.objects.filter(
        university=university
    ).exclude(id=course.id).order_by('level')[:5]

    context = {
        'university': university,
        'course': course,
        'related_courses': related_courses,
    }
    return render(request, 'universities/course_detail.html', context)


# ─── SCHOLARSHIP LIST ─────────────────────────────────────────────────────────

def scholarship_list(request):
    scholarships = Scholarship.objects.select_related('university', 'university__state')

    state_filter = request.GET.get('state')
    type_filter = request.GET.get('type')
    level_filter = request.GET.get('level')
    search_q = request.GET.get('q', '').strip()

    if state_filter:
        scholarships = scholarships.filter(university__state__slug=state_filter)
    if type_filter:
        scholarships = scholarships.filter(scholarship_type=type_filter)
    if level_filter:
        scholarships = scholarships.filter(eligible_levels__icontains=level_filter)
    if search_q:
        scholarships = scholarships.filter(
            Q(name__icontains=search_q) |
            Q(university__name__icontains=search_q)
        )

    scholarships = scholarships.order_by('-coverage_percentage', 'name')
    paginator = Paginator(scholarships, 15)
    page = request.GET.get('page')
    scholarships_page = paginator.get_page(page)

    states = State.objects.order_by('name')

    context = {
        'scholarships': scholarships_page,
        'states': states,
        'state_filter': state_filter,
        'type_filter': type_filter,
        'level_filter': level_filter,
        'search_q': search_q,
        'total_results': paginator.count,
    }
    return render(request, 'universities/scholarship_list.html', context)


# ─── SEARCH ──────────────────────────────────────────────────────────────────

def search(request):
    query = request.GET.get('q', '').strip()
    results = {'universities': [], 'courses': [], 'scholarships': []}

    if query:
        results['universities'] = University.objects.filter(
            Q(name__icontains=query) |
            Q(city__name__icontains=query) |
            Q(state__name__icontains=query) |
            Q(description__icontains=query) |
            Q(popular_courses__icontains=query)
        ).select_related('state', 'city')[:10]

        results['courses'] = Course.objects.filter(
            Q(name__icontains=query) |
            Q(field_of_study__icontains=query) |
            Q(university__name__icontains=query)
        ).select_related('university')[:10]

        results['scholarships'] = Scholarship.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        ).select_related('university')[:5]

    context = {
        'query': query,
        'results': results,
        'total_results': len(results['universities']) + len(results['courses']) + len(results['scholarships']),
    }
    return render(request, 'universities/search_results.html', context)


# ─── AJAX SEARCH AUTOCOMPLETE ─────────────────────────────────────────────────

@require_GET
def search_autocomplete(request):
    q = request.GET.get('q', '').strip()
    if len(q) < 2:
        return JsonResponse({'results': []})

    universities = University.objects.filter(name__icontains=q).values('name', 'slug')[:5]
    courses = Course.objects.filter(name__icontains=q).values('name', 'slug', 'university__slug')[:5]

    results = []
    for u in universities:
        results.append({'type': 'university', 'label': u['name'], 'url': f"/universities/{u['slug']}/"})
    for c in courses:
        results.append({'type': 'course', 'label': c['name'], 'url': f"/universities/{c['university__slug']}/courses/{c['slug']}/"})

    return JsonResponse({'results': results})


# ─── COMPARE ─────────────────────────────────────────────────────────────────

def compare(request):
    slugs = request.GET.getlist('uni')
    universities = []
    if slugs:
        universities = University.objects.filter(slug__in=slugs).prefetch_related('courses', 'scholarships')

    all_universities = University.objects.values('name', 'slug').order_by('name')

    context = {
        'universities': universities,
        'all_universities': all_universities,
        'selected_slugs': slugs,
    }
    return render(request, 'universities/compare.html', context)


# ─── BOOKMARK ────────────────────────────────────────────────────────────────

def toggle_bookmark(request, uni_slug):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    university = get_object_or_404(University, slug=uni_slug)

    bookmark, created = Bookmark.objects.get_or_create(session_key=session_key, university=university)
    if not created:
        bookmark.delete()
        action = 'removed'
    else:
        action = 'added'

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'action': action})
    return redirect('university_detail', slug=uni_slug)


def bookmark_list(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    bookmarks = Bookmark.objects.filter(session_key=session_key).select_related(
        'university', 'university__state', 'university__city'
    )
    return render(request, 'universities/bookmarks.html', {'bookmarks': bookmarks})


# ─── STATIC PAGES (ADSENSE COMPLIANCE) ───────────────────────────────────────

def about(request):
    return render(request, 'pages/about.html')

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def contact(request):
    return render(request, 'pages/contact.html')

def disclaimer(request):
    return render(request, 'pages/disclaimer.html')

def visa_guide(request):
    return render(request, 'pages/visa_guide.html')

def english_comparison(request):
    return render(request, 'pages/english_comparison.html')
    
def faq(request):
    return render(request, 'pages/faq.html')

def terms(request):
    return render(request, 'pages/terms.html')
    
    def sop_guide(request):
    return render(request, 'pages/sop_guide.html')
