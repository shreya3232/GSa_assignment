from django.db import models
# from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Task(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.name
