from django import forms
from .models import ContactMessage, Client, Project, Service, Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_title', 'quote', 'avatar_initials', 'stars']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g. John Doe'}),
            'client_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. CEO of TechCorp'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'What did the client say?'}),
            'avatar_initials': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2, 'placeholder': 'e.g. JD'}),
            'stars': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon_name', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g. Web Development'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description of this service...'}),
            'icon_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g. 'code-2' (Lucide icon name)"}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'technologies', 'description', 'image_style', 'link', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g. Vortex E-commerce Platform'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Web Design, Mobile App'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g. React • Node.js • MongoDB"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Briefly describe the project...'}),
            'image_style': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can we help?', 'rows': 5}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'industry', 'total_spent', 'health_status', 'logo_color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'total_spent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'health_status': forms.Select(attrs={'class': 'form-control'}),
            'logo_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control', 'style': 'height: 40px;'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'client', 'project_id', 'progress', 'deadline', 'status', 'health', 'category', 'image_style']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project_id': forms.TextInput(attrs={'class': 'form-control'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Design, Development'}),
            'health': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'image_style': forms.Select(attrs={'class': 'form-control'}),
        }
