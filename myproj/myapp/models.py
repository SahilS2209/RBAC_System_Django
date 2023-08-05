from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.hashers import check_password as django_check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class API(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    created_by = models.ForeignKey('MyUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    mapped_apis = models.ManyToManyField(API)
    
    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)

class StorableToken(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user.username}"

class CustomAccessToken(AccessToken):
    def save(self, *args, **kwargs):
        token = super().save(*args, **kwargs)
        StorableToken.objects.create(user=self.user, token=self.token)
        return token

class CustomRefreshToken(RefreshToken):
    def save(self, *args, **kwargs):
        token = super().save(*args, **kwargs)
        StorableToken.objects.create(user=self.user, token=self.token)
        return token
    
