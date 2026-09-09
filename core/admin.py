from django.contrib import admin
from .models import Project, Skill, Certificate, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order']
    list_editable = ['featured', 'order']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage', 'order']
    list_editable = ['percentage', 'order']
    list_filter = ['category']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'date', 'order']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
