from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView,RedirectView
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from .models import Group,GroupMember
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreateGroupView(CreateView,LoginRequiredMixin):
	model = Group
	fields=('name','discription'
		)
	# success_url=reverse_lazy('accounts:test')

	def form_valid(self,form):
		self.object=form.save(commit=False)
		self.object.user=self.request.user
		self.object.save()
		GroupMember.objects.create(user=self.object.user,group=self.object)
		return super().form_valid(form)

class GroupListView(ListView,LoginRequiredMixin):
	model=Group


class SingleGroupview(DetailView,LoginRequiredMixin):
	model=Group

class DeleteGroupView(DeleteView,LoginRequiredMixin):
	model=Group
	success_url=reverse_lazy('groups:list')

class JoinGroupView(LoginRequiredMixin,RedirectView):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})


	def get(self,request,*args,**kwargs):
		group=get_object_or_404(Group,slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user,group=group)

		except IntegrityError:
			messages.warning(self.request,'warning already')

		else:
			messages.success(self.request,'you are the member of the group')

		return super().get(request,*args,**kwargs)

class LeaveGroupView(RedirectView,LoginRequiredMixin):

	def get_redirect_url(self,*args,**kwargs):
		return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})


	def get(self,request,*args,**kwargs):
		

		membership=GroupMember.objects.filter(
		user=self.request.user,
		group__slug=self.kwargs.get('slug')).get()

		membership.delete()

		return super().get(request,*args,**kwargs)





			