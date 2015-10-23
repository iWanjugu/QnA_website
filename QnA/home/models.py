from django.db import models

# Create your models here.
class Users (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.Charfield(label="Brief description", max_length=200)
    interests = models.TextField(label="Brief description")
    registered_date = models.DateField(auto_now=False, auto_now_add=True)
    last_update = models.DateField(auto_now=True, auto_now_add=False)

