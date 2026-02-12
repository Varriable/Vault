from django.db import models
from django.contrib.auth.models import AbstractUser

from secret.models import Secret

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = None
    email = models.EmailField(unique = True, max_length=100, required=True)
    name = models.CharField(max_length=100, required=True)
    password = models.CharField(max_length=100, required=True)

    USERNAME_FIELD = 'email'


    def __str__(self):
        return f"User {self.id} - {self.name}"    

class Otp(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=6, required=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP {self.id} for User {self.user.name} - Code: {self.code}"

 