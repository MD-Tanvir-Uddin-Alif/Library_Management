from django.urls import path
from .import views

urlpatterns = [
    path('registration/',views.Registrationview,name="Registration_page"),
    path('login/',views.LoginView,name="Login_page"),
    path('logout/',views.LogoutView,name="Logout_page"),
    path('profil/',views.user_profieView,name="Profile_page"),
]
