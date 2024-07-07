from django.urls import path, include  # Ensure 'include' is imported

from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create_user/', views.create_user_view, name='create_user'),
    path('', views.home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include function used here
    # other paths...
]
