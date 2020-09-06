from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
# Create your models here.
class User(User,PermissionsMixin):
	def __str__(self):
		return self.username

# class ProfileUser(models.Model):
# 	name=models.CharField(max_length=20)
# 	address=models.TextField()
# 	phone_no=models.IntegerField()
# 	Profile_photo=models.ImageField(upload_to='images',blank = True,null = True)
# 	user=models.ForignKey(User,related_name='profile_user')

# 	def __str__(self):
# 		return self.name