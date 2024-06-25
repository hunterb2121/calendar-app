from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Permissions(models.Model):
    permission_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.permission_name


class Calendar(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    alert_time = models.DurationField()
    created_date = models.DateTimeField(auto_now_add=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SharedCalendar(models.Model):
    primary_user = models.ForeignKey(User, related_name='primary_user', on_delete=models.CASCADE)
    shared_user = models.ForeignKey(User, related_name='shared_user', on_delete=models.CASCADE)
    secondary_permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.primary_user.username} shares {self.calendar.title} with {self.shared_user.username}'