"""AusUni Admin Configuration"""

from django.contrib import admin
from django.utils.html import format_html
from .models import State, City, University, Campus, Course, Scholarship, Bookmark


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'capital', 'university_count']
    search_fields = ['name', 'abbreviation']
    prepopulated_fields = {'slug': ('name',)}

    def university_count(self, obj):
        return obj.universities.count()
    university_count.short_description = 'Universities'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'cost_of_living', 'university_count']
    list_filter = ['state']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

    def university_count(self, obj):
        return obj.universities.count()
    university_count.short_description = 'Universities'


class CampusInline(admin.TabularInline):
    model = Campus
    extra = 1
    fields = ['name', 'city', 'is_main', 'address']


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0
    fields = ['name', 'level', 'tuition_fee_annual', 'ielts_overall', 'official_url']
    show_change_link = True


class ScholarshipInline(admin.TabularInline):
    model = Scholarship
    extra = 0
    fields = ['name', 'coverage', 'coverage_percentage', 'official_url']
    show_change_link = True


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'short_name', 'state', 'city',
        'institution_type', 'group_affiliation',
        'ranking_qs', 'is_featured', 'course_count', 'scholarship_count'
    ]
    list_filter = ['state', 'institution_type', 'group_affiliation', 'is_featured']
    search_fields = ['name', 'short_name', 'city__name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured']
    inlines = [CampusInline, ScholarshipInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_name', 'slug', 'state', 'city',
                       'institution_type', 'group_affiliation', 'established_year')
        }),
        ('Description', {
            'fields': ('description', 'about', 'popular_courses', 'internship_info')
        }),
        ('Rankings & Statistics', {
            'fields': ('ranking_qs', 'ranking_times', 'total_students', 'international_students')
        }),
        ('Financial', {
            'fields': ('cost_of_living', 'application_fee')
        }),
        ('Official Links', {
            'fields': ('official_website', 'international_page', 'scholarship_page', 'application_portal')
        }),
        ('Display', {
            'fields': ('logo', 'image', 'is_featured')
        }),
    )

    def course_count(self, obj):
        count = obj.courses.count()
        return format_html('<span style="color: green;">{}</span>', count)
    course_count.short_description = 'Courses'

    def scholarship_count(self, obj):
        count = obj.scholarships.count()
        return format_html('<span style="color: blue;">{}</span>', count)
    scholarship_count.short_description = 'Scholarships'


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'city', 'state', 'is_main']
    list_filter = ['state', 'is_main']
    search_fields = ['name', 'university__name', 'city__name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'university', 'level', 'tuition_fee_annual',
        'ielts_overall', 'intake_months', 'is_popular'
    ]
    list_filter = ['level', 'study_mode', 'is_popular', 'university__state']
    search_fields = ['name', 'university__name', 'field_of_study']
    list_editable = ['is_popular']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['campus']

    fieldsets = (
        ('Basic Information', {
            'fields': ('university', 'campus', 'name', 'slug', 'level', 'field_of_study',
                       'duration', 'study_mode', 'is_popular')
        }),
        ('Fees', {
            'fields': ('tuition_fee_annual', 'tuition_fee_total', 'tuition_note')
        }),
        ('Intakes', {
            'fields': ('intake_months', 'next_intake')
        }),
        ('Academic Requirements', {
            'fields': ('academic_requirement', 'gpa_requirement')
        }),
        ('English Requirements', {
            'fields': ('ielts_overall', 'ielts_min_band', 'pte_overall', 'toefl_ibt')
        }),
        ('Details', {
            'fields': ('description', 'course_structure', 'career_outcomes')
        }),
        ('Links', {
            'fields': ('official_url', 'apply_url')
        }),
    )


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'university', 'scholarship_type', 'coverage',
        'coverage_percentage', 'deadline'
    ]
    list_filter = ['scholarship_type', 'university__state']
    search_fields = ['name', 'university__name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'university', 'course', 'created_at']
    list_filter = ['created_at']

# Admin site customisation
admin.site.site_header = 'AusUni Administration'
admin.site.site_title = 'AusUni Admin'
admin.site.index_title = 'Manage Australian University Data'
