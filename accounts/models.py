from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Account(AbstractUser):
	# user 					=	models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	id						=   models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
	email 					=   models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				=   models.CharField(max_length=30, unique=True)
	date_joined				=   models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				=   models.DateTimeField(verbose_name='last login', auto_now=True)

	REQUIRED_FIELD='email'
	USERNAME_FIELD='username'

	def __str__(self):
		return self.username
	class Meta:
		ordering=['date_joined']
	@property
	def imageURL(self):
		try:
			url = self.profile_image.url
		except:
			url = ''
		return url	