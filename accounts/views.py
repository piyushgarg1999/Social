from django.shortcuts import render,get_object_or_404,redirect
from accounts.forms import Signup
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.

class Registerview(CreateView):
	form_class=Signup
	template_name='accounts/register.html'
	success_url=reverse_lazy('accounts:test')
	
# class TemplateTestView(LoginRequiredMixin,ListView):
# 	model = FoodItem
# 	template_name='food/food_list.html'
	
class TemplateTestView(TemplateView):
	template_name='accounts/test.html'

class LogoutView(TemplateView):
	template_name='accounts/afterlogout.html'

# Create your views here.

class ProfileUser(TemplateView):
	template_name='accounts/profile_form.html'
