from django.db import models

from apps.user.models import User

class Secret(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='secrets')
    title = models.CharField(max_length=100 )
    key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Secret {self.id} - {self.title} (User: {self.user.name})"
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'title']),
        ]


class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE, related_name='otps', null=True, blank=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP {self.id} for User {self.user.name} - Code: {self.code}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'code']),
        ]