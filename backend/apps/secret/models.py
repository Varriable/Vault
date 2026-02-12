from django.db import models
from user.models import User

class Secret(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='secrets')
    title = models.CharField(max_length=100, required=True)
    key = models.TextField(required=True)

    def __str__(self):
        return f"Secret {self.id} - {self.title} (User: {self.user.name})"
