from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from Group import views
from django.conf.urls.static import static
from django.conf import settings

app_name='groups'


urlpatterns = [
       path('new_group_create/', views.CreateGroupView.as_view(),name='CreateGroup'),
       path('group_list/',views.GroupListView.as_view(),name='list'),
       path('group_detail/<slug:slug>/',views.SingleGroupview.as_view(),name='single'),
       path('join_group/<slug:slug>',views.JoinGroupView.as_view(),name='join_group'),
       path('leave_group/<slug:slug>',views.LeaveGroupView.as_view(),name='leave_group'),
       path('delete_group/<slug:slug>',views.DeleteGroupView.as_view(),name='delete_group'),
]