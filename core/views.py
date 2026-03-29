from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm, ClientForm, ProjectForm, ServiceForm
from .models import Service, Project, Testimonial, Client

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

def pricing_view(request):
    return render(request, 'core/pricing.html')

def contact_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        if first_name or last_name:
            data['name'] = f"{first_name} {last_name}".strip()
            
        form = ContactForm(data)
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
    return render(request, 'core/dashboard.html', {'active_tab': 'dashboard'})

@login_required
def clients_view(request):
    client_form = ClientForm()
    return render(request, 'core/clients.html', {'active_tab': 'clients', 'client_form': client_form})

@login_required
def projects_view(request):
    projects = Project.objects.all().order_by('-id')
    client_form = ClientForm()
    project_form = ProjectForm()
    context = {
        'active_tab': 'projects',
        'projects': projects,
        'client_form': client_form,
        'project_form': project_form,
    }
    return render(request, 'core/projects.html', context)

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully.')
        else:
            messages.error(request, 'Failed to add client. Please check the form.')
    return redirect('core:projects')

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully.')
        else:
            messages.error(request, 'Failed to add project. Please check the form.')
    return redirect('core:projects')

# ─── Services CRUD ──────────────────────────────────────────────
@login_required
def services_manager(request):
    all_services = Service.objects.all().order_by('order')
    form = ServiceForm()
    return render(request, 'core/services_manager.html', {
        'active_tab': 'services',
        'services': all_services,
        'form': form,
    })

@login_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully.')
        else:
            messages.error(request, 'Failed to add service.')
    return redirect('core:services_manager')

@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully.')
        else:
            messages.error(request, 'Failed to update service.')
    return redirect('core:services_manager')

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, f'Service "{service.title}" deleted.')
    return redirect('core:services_manager')

