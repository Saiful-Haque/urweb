from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """Custom User model for URWEB to support client portal features."""
    is_client = models.BooleanField(default=False)
    company_name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g., 'code-2')")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image_style = models.CharField(max_length=50, choices=[('dark', 'Dark'), ('light', 'Light'), ('accent', 'Accent')], default='accent')
    link = models.CharField(max_length=200, default="#")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    quote = models.TextField()
    avatar_initials = models.CharField(max_length=2)
    stars = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.client_name
