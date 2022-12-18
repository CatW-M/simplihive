from django.urls import path
from .import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    ]