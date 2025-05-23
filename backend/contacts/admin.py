from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
