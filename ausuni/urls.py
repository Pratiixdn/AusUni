"""AusUni URL Configuration"""

from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from universities.sitemaps import UniversitySitemap, CourseSitemap, StateSitemap

sitemaps = {
    'universities': UniversitySitemap,
    'courses': CourseSitemap,
    'states': StateSitemap,
}

def ads_txt(request):
    content = "google.com, pub-8936104184201511, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(content, content_type='text/plain') 

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('ads.txt', ads_txt),
    path('admin/', admin.site.urls),
    path('', include('universities.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
