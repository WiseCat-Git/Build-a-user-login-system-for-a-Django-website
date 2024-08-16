"""
URL configuration for lushlyrics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# lushlyrics/urls.py

from django.contrib import admin
from django.urls import path, include
from lushlyrics.users import views as user_views
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings  # Add this import
from django.conf.urls.static import static  # Add this import

def redirect_to_home_or_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('login'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home_or_login),  # Redirect root URL based on authentication status
    path('home/', user_views.home, name='home'),  # Home page for authenticated users
    path('register/', user_views.register, name='register'),
    path('thank-you/', user_views.thank_you, name='thank_you'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('', include('lushlyrics.users.urls')),
    path('registration-confirmation/', user_views.registration_confirmation, name='registration_confirmation'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
