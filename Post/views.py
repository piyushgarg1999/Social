from django.shortcuts import render
from django.urls import reverse,reverse_lazy
# Create your views here.
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
user=get_user_model()
from Group.models import Group
from django.http import Http404
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.auth.models import User


class PostList(LoginRequiredMixin,SelectRelatedMixin,ListView):
	model=Post
	select_related=('user','group',)

class UserPostList(LoginRequiredMixin,ListView):
	model = Post
	template_name='Post/user_post_list.html'

	def get_queryset(self):
		try:
			self.post_user=User.objects.prefetch_related('post').get(username__iexact=self.kwargs.get('username'))

		except User.DoesNotExist:
			raise Http404

		else:
			return self.post_user.post.all()

class PostDetailView(LoginRequiredMixin,SelectRelatedMixin,DetailView):
		model=Post
		select_related=('user','group')

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=('message','group')


	def form_valid(self,form,**kwargs):
		self.object=form.save(commit=False)
		self.object.user=self.request.user
		self.object.save()
		return super().form_valid(form)


class MyPostCreateViewForm(LoginRequiredMixin,CreateView):
	model=Post
	fields=('message',)
	
	def form_valid(self,form,):
		self.object=form.save(commit=False)
		self.object.user=self.request.user
		
		self.object.group=Group.objects.get(pk=self.kwargs['pk'])
		self.object.save()
		return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin,DeleteView):
	model=Post
	success_url=reverse_lazy('posts:all_post')



