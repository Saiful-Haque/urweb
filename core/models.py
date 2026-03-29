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
    is_read = models.BooleanField(default=False)
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

class Client(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    health_status = models.CharField(max_length=20, choices=[('ON TRACK', 'On Track'), ('DELAYED', 'Delayed'), ('INACTIVE', 'Inactive')], default='ON TRACK')
    logo_color = models.CharField(max_length=50, default='#111827')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100)
    technologies = models.CharField(max_length=200, blank=True, help_text="e.g., 'React • Node.js'")
    description = models.TextField(blank=True)
    image_style = models.CharField(max_length=50, choices=[('dark', 'Dark'), ('light', 'Light'), ('accent', 'Accent')], default='accent')
    link = models.CharField(max_length=200, default="#")
    order = models.PositiveIntegerField(default=0)
    
    # SaaS Management Fields
    project_id = models.CharField(max_length=20, blank=True, help_text="e.g., PRJ-9402")
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    progress = models.IntegerField(default=0, help_text="0 to 100")
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Consultation', help_text="e.g., Development, Design, Launch")
    health = models.CharField(max_length=20, default='Green', choices=[('Green', 'Green'), ('Yellow', 'Yellow'), ('Red', 'Red')])


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
