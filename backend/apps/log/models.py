from django.db import models

from apps.user.models import User

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.id} for User {self.user.name} - Action: {self.action} at {self.timestamp}"  

    class Meta:
        indexes = [
            models.Index(fields=['user', 'action']),
        ]