from django.urls import path

from cart import views
app_name = 'cart'
urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path(r'^add/(?P<id>\d+)', views.add_to_cart, name='add_to_cart'),
    path(r'^adjust/(?P<id>\d+)', views.adjust_cart, name='adjust_cart'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
]
