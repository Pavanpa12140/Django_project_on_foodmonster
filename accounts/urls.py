from django.urls import path
from .forms import userForm
from accounts import views

app_name='nava'

urlpatterns = [
    path('registerUser/',views.registerUser,name='registerUser'),
    path('registerVender/',views.registerVendor,name='registerVender'),
    path('user_login/',views.user_login,name='user_login'),
    path('dashboard/',views.dashboard,name='dashboard/'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('dashboardvender/',views.dashboardvender,name='dashboardvender/'),
]