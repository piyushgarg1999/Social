from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

app_name='accounts'


urlpatterns = [
       
       path('',auth_view.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
       path('password_change/',auth_view.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),name='password_change'),
       path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_changed'),
       path('logout/',auth_view.LogoutView.as_view(),name = 'logout'),
       path('register_user/',views.Registerview.as_view(),name = 'register'),
       path('afterlogout/',views.LogoutView.as_view(),name='afterlogout'),
       path('test/',views.TemplateTestView.as_view(),name = 'test'),
       path('profile_user',views.ProfileUser.as_view(),name='profile_user'),
       path('email_message/',views.Email_Massage,name='email_message'),
      ]