from django.contrib import admin
from taskmanagement.models import Task
# Register your models here.
@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display=('title','description','completed')