"""
AusUni Models
Comprehensive database schema for Australian University Portal
"""

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class State(models.Model):
    """Australian states and territories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    capital = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=200, blank=True, help_text="Image filename in static/img/states/")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('state_detail', kwargs={'slug': self.slug})


class City(models.Model):
    """Cities within Australian states"""
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    description = models.TextField(blank=True)
    population = models.CharField(max_length=50, blank=True)
    cost_of_living = models.CharField(max_length=50, blank=True, help_text="e.g. AUD 1,800–2,500/month")

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Cities'
        unique_together = ('slug', 'state')

    def __str__(self):
        return f"{self.name}, {self.state.abbreviation}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'state_slug': self.state.slug, 'city_slug': self.slug})


class University(models.Model):
    """Australian universities – public, private, TAFE"""

    TYPE_CHOICES = [
        ('public', 'Public University'),
        ('private', 'Private University'),
        ('tafe', 'TAFE Institute'),
        ('private_provider', 'Private Provider'),
    ]

    GROUP_CHOICES = [
        ('go8', 'Group of Eight (Go8)'),
        ('atn', 'Australian Technology Network (ATN)'),
        ('irua', 'Innovative Research Universities (IRU)'),
        ('raa', 'Regional Universities Australia'),
        ('none', 'Independent'),
    ]

    # Basic info
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_name = models.CharField(max_length=50, blank=True, help_text="e.g. UNSW, ANU")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='universities')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='universities')
    institution_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='public')
    group_affiliation = models.CharField(max_length=20, choices=GROUP_CHOICES, default='none')

    # Details
    established_year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    about = models.TextField(blank=True, help_text="Why choose this university")
    ranking_qs = models.CharField(max_length=50, blank=True, help_text="e.g. #41 World")
    ranking_times = models.CharField(max_length=50, blank=True)
    total_students = models.CharField(max_length=50, blank=True)
    international_students = models.CharField(max_length=50, blank=True)

    # Financial
    cost_of_living = models.CharField(max_length=100, blank=True, help_text="e.g. AUD 1,800–2,500/month")
    application_fee = models.CharField(max_length=50, blank=True)

    # Links
    official_website = models.URLField()
    international_page = models.URLField(blank=True)
    scholarship_page = models.URLField(blank=True)
    application_portal = models.URLField(blank=True)

    # Media
    logo = models.CharField(max_length=200, blank=True, help_text="Logo filename")
    image = models.CharField(max_length=200, blank=True, help_text="Campus image filename")

    # Meta
    popular_courses = models.CharField(max_length=500, blank=True, help_text="Comma-separated popular courses")
    internship_info = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('university_detail', kwargs={'slug': self.slug})

    @property
    def is_go8(self):
        return self.group_affiliation == 'go8'

    @property
    def type_badge_class(self):
        return {
            'public': 'badge-public',
            'private': 'badge-private',
            'tafe': 'badge-tafe',
            'private_provider': 'badge-private',
        }.get(self.institution_type, 'badge-public')


class Campus(models.Model):
    """University campuses"""
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='campuses')
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='campuses')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    is_main = models.BooleanField(default=False)
    facilities = models.TextField(blank=True, help_text="Comma-separated list of facilities")
    map_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-is_main', 'name']
        verbose_name_plural = 'Campuses'

    def __str__(self):
        return f"{self.university.short_name or self.university.name} – {self.name}"


class Course(models.Model):
    """Individual courses offered at universities"""

    LEVEL_CHOICES = [
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor'),
        ('honours', 'Honours'),
        ('graduate_cert', 'Graduate Certificate'),
        ('graduate_diploma', 'Graduate Diploma'),
        ('master', 'Master'),
        ('phd', 'PhD / Doctorate'),
    ]

    STUDY_MODE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('online', 'Online'),
        ('blended', 'Blended'),
    ]

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    campus = models.ManyToManyField(Campus, blank=True, related_name='courses')

    # Course info
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    field_of_study = models.CharField(max_length=200, blank=True, help_text="e.g. Information Technology, Business")
    duration = models.CharField(max_length=100, help_text="e.g. 3 years, 2 years")
    study_mode = models.CharField(max_length=20, choices=STUDY_MODE_CHOICES, default='full_time')

    # Fees
    tuition_fee_annual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                              help_text="Annual fee in AUD")
    tuition_fee_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                             help_text="Total program fee in AUD")
    tuition_note = models.CharField(max_length=200, blank=True, help_text="e.g. per year, 2024 indicative")

    # Intakes
    intake_months = models.CharField(max_length=200, help_text="e.g. February, July")
    next_intake = models.CharField(max_length=100, blank=True)

    # Academic requirements
    academic_requirement = models.TextField(help_text="e.g. Minimum 65% in Bachelor's")
    gpa_requirement = models.CharField(max_length=100, blank=True, help_text="e.g. 3.0/4.0 GPA")

    # English requirements
    ielts_overall = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    ielts_min_band = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True,
                                          help_text="Minimum per band")
    pte_overall = models.IntegerField(null=True, blank=True)
    toefl_ibt = models.IntegerField(null=True, blank=True)

    # Outcomes
    career_outcomes = models.TextField(blank=True, help_text="Career pathways")
    course_structure = models.TextField(blank=True, help_text="Brief course structure description")
    description = models.TextField(blank=True)

    # Links
    official_url = models.URLField(help_text="MANDATORY: Official course page URL")
    apply_url = models.URLField(blank=True)

    # Meta
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['level', 'name']

    def __str__(self):
        return f"{self.name} – {self.university.short_name or self.university.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'uni_slug': self.university.slug, 'course_slug': self.slug})

    @property
    def level_display_short(self):
        return {
            'bachelor': 'Bachelor',
            'master': 'Master',
            'phd': 'PhD',
            'diploma': 'Diploma',
            'certificate': 'Certificate',
            'honours': 'Honours',
            'graduate_cert': 'Grad Cert',
            'graduate_diploma': 'Grad Diploma',
        }.get(self.level, self.level.title())


class Scholarship(models.Model):
    """Scholarships available at universities"""

    TYPE_CHOICES = [
        ('merit', 'Merit-based'),
        ('need', 'Need-based'),
        ('destination', 'Destination/Country'),
        ('course', 'Course-specific'),
        ('government', 'Government'),
        ('partial', 'Partial Tuition'),
        ('full', 'Full Tuition'),
    ]

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='scholarships')
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    scholarship_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='merit')

    # Coverage
    coverage = models.CharField(max_length=200, help_text="e.g. 25% tuition fee reduction, AUD 10,000")
    coverage_percentage = models.IntegerField(null=True, blank=True, help_text="e.g. 25 for 25%")

    # Criteria
    eligibility = models.TextField(help_text="Who is eligible")
    academic_requirement = models.CharField(max_length=300, blank=True)
    eligible_courses = models.CharField(max_length=500, blank=True, help_text="Comma-separated course types or 'All courses'")
    eligible_levels = models.CharField(max_length=200, blank=True, help_text="e.g. Bachelor, Master")

    # Deadline
    deadline = models.CharField(max_length=200, blank=True, help_text="e.g. 30 November 2025 or Intake-based")
    intake_deadline = models.BooleanField(default=False, help_text="Deadline tied to intake")

    # Links
    official_url = models.URLField(help_text="Official scholarship page")
    apply_url = models.URLField(blank=True)

    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-coverage_percentage', 'name']

    def __str__(self):
        return f"{self.name} – {self.university.short_name or self.university.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Bookmark(models.Model):
    """Session-based bookmarks for universities and courses"""
    session_key = models.CharField(max_length=40)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('session_key', 'university'), ('session_key', 'course')]

    def __str__(self):
        if self.university:
            return f"Bookmark: {self.university.name}"
        return f"Bookmark: {self.course.name}"
