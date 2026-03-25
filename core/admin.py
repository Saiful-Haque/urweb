from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ContactMessage, Service, Project, Testimonial, User

# Register your models here.
admin.site.register(User, UserAdmin)

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('name', 'email', 'subject')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_editable = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_title', 'stars')
