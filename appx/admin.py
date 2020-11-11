from django.contrib import admin
from .models import Repository, Commits
admin.site.register(Repository)
admin.site.register(Commits)
# Register your models here.
