from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'email', 'university', 'submitted_at')
    search_fields = ('student_name', 'email', 'phone')
