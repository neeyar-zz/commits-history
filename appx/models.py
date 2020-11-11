from django.db import models
from datetime import datetime

class Repository(models.Model):    
    full_name=models.CharField(max_length=100)    
    description=models.CharField(max_length=255)
    created_at=models.DateField()
    owner_login=models.CharField(max_length=50, null=True)
    url=models.URLField(max_length=255)

class Commits(models.Model):
    repo_full_name=models.CharField(max_length=100, primary_key=True)
    full=models.TextField()

