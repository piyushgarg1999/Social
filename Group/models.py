from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()



class Group(models.Model):
	name = models.CharField(max_length=20,unique=True)
	user=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='mygroup')
	slug=models.SlugField(unique=True)
	discription=models.TextField(blank=True,default='')
	members = models.ManyToManyField(User,through='GroupMember')

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('groups:single',kwargs={'slug':self.slug},)


	class Meta():
		ordering=['name']
		

class GroupMember(models.Model):
	group=models.ForeignKey(Group,related_name='membership',on_delete=models.CASCADE)
	user=models.ForeignKey(User,related_name='user_group',on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together=['group','user']