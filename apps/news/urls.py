from django.urls import path

from apps.news.views import *

app_name="news"

urlpatterns = [
    path('', home_page, name="home"),
    path('contact', contact_page, name="contact"),
    path('404', page_notfound, name="page-notfound"),
    path('single_page<id>', single_page, name="single"),
    path('about', about, name='about')
]
