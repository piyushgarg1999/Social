from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from Post import views
from django.conf.urls.static import static
from django.conf import settings

app_name='posts'


urlpatterns = [
       
       path('allpost_/',views.PostList.as_view(),name='all_post'),
       path('user_post/(?P<username>[-\w]+)/',views.UserPostList.as_view(),name='user_post'),
       path('user_post/(?P<username>[-\w]+)/(<int:pk>)',views.PostDetailView.as_view(),name='single'),
       path('new_create_post/',views.PostCreateView.as_view(),name='create_post'),
       path('delete_post/<int:pk>',views.PostDeleteView.as_view(),name='delete_post'),
       path('new_create_post_form/<int:pk>/',views.MyPostCreateViewForm.as_view(),name='create_post_form'),

    ]
