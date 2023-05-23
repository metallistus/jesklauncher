from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Profile(models.Model):
   MOTIVATE_CONTENT = (
      ('text', 'text'),
      ('image', 'image'),
   )
   
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   image = models.FileField(upload_to='motivate-content/', blank=True)
   text = models.CharField(max_length=100, blank=True)
   
   google_token = models.CharField(max_length=1500, blank=True)
   
   def __str__(self):
      return self.user.username
   
class Todo(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   message = models.CharField(max_length=500, default='')
   
   created_at = models.DateTimeField('Created Time', auto_now_add = True, null=True)
   updated_at = models.DateTimeField(auto_now=True, null=True)
   
   def __str__(self):
      return self.user.username