from django.urls import path

from . import views
app_name = 'home'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('best_sellers/', views.bestselling),
    path('fiction_books/', views.fiction),
    path('authors/', views.authors),
    path('study_books/', views.studybooks),
]
