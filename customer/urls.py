from django.urls import path

from . import views
app_name = 'customer'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('customer/', views.customer, name='customer_page'),
    path('login/', views.viewlogin, name='login'),
    path('logout/', views.viewlogout, name='logout'),
]