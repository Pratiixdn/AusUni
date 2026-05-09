"""AusUni URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Search
    path('search/', views.search, name='search'),
    path('api/search/autocomplete/', views.search_autocomplete, name='search_autocomplete'),

    # Compare
    path('compare/', views.compare, name='compare'),

    # Bookmarks
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
    path('bookmarks/toggle/<slug:uni_slug>/', views.toggle_bookmark, name='toggle_bookmark'),

    # Universities
    path('universities/', views.university_list, name='university_list'),
    path('universities/<slug:slug>/', views.university_detail, name='university_detail'),
    path('universities/<slug:uni_slug>/courses/<slug:course_slug>/', views.course_detail, name='course_detail'),

    # Courses
    path('courses/', views.course_list, name='course_list'),

    # Scholarships
    path('scholarships/', views.scholarship_list, name='scholarship_list'),

    # States and Cities
    path('australia/<slug:slug>/', views.state_detail, name='state_detail'),
    path('australia/<slug:state_slug>/<slug:city_slug>/', views.city_detail, name='city_detail'),

    # Static pages
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/', views.contact, name='contact'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
