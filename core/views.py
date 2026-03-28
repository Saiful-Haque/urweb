from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
from .models import Service, Project, Testimonial

# Create your views here.
def home(request):
    services = Service.objects.all()[:6]  # Show only first 6 on home page
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)

def services_view(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def portfolio_view(request):
    projects = Project.objects.all()
    categories = Project.objects.order_by('category').values_list('category', flat=True).distinct()
    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'core/portfolio.html', context)

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            
            # Send Notification Email
            subject = f"New Lead: {contact_instance.subject}"
            email_context = {
                'name': contact_instance.name,
                'email': contact_instance.email,
                'subject': contact_instance.subject,
                'message': contact_instance.message,
                'timestamp': contact_instance.created_at,
            }
            email_body = render_to_string('core/emails/contact_notification.txt', email_context)
            
            try:
                send_mail(
                    subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL_NOTIFICATION],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")

            messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html')
