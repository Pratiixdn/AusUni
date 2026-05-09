"""AusUni Sitemaps for SEO"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import University, Course, State


class UniversitySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return University.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class CourseSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Course.objects.select_related('university').all()

    def location(self, obj):
        return f'/universities/{obj.university.slug}/courses/{obj.slug}/'


class StateSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return State.objects.all()

    def location(self, obj):
        return f'/australia/{obj.slug}/'
