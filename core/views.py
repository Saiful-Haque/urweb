from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm, ClientForm, ProjectForm, ServiceForm, PortfolioForm, TestimonialForm
from .models import Service, Project, Testimonial, Client, ContactMessage, User

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

@staff_member_required
def dashboard_view(request):
    total_clients = Client.objects.count()
    ongoing_projects = Project.objects.exclude(status__iexact='Launched').count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    recent_projects = Project.objects.all().order_by('-id')[:5]
    recent_logins = User.objects.filter(last_login__isnull=False).order_by('-last_login')[:5]
    recent_inquiries = ContactMessage.objects.all().order_by('-created_at')[:3]
    
    context = {
        'active_tab': 'dashboard',
        'total_clients': total_clients,
        'ongoing_projects': ongoing_projects,
        'unread_messages': unread_messages,
        'recent_projects': recent_projects,
        'recent_logins': recent_logins,
        'recent_inquiries': recent_inquiries,
    }
    return render(request, 'core/dashboard.html', context)

@staff_member_required
def clients_view(request):
    clients = Client.objects.all().order_by('-id')
    client_form = ClientForm()
    return render(request, 'core/clients.html', {
        'active_tab': 'clients', 
        'clients': clients,
        'client_form': client_form
    })

@staff_member_required
def projects_view(request):
    projects = Project.objects.all().order_by('-id')
    clients = Client.objects.all().order_by('name')
    client_form = ClientForm()
    project_form = ProjectForm()
    context = {
        'active_tab': 'projects',
        'projects': projects,
        'clients': clients,
        'client_form': client_form,
        'project_form': project_form,
    }
    return render(request, 'core/projects.html', context)

@staff_member_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully.')
        else:
            messages.error(request, 'Failed to add client. Please check the form.')
    return redirect('core:clients')

@staff_member_required
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully.')
        else:
            messages.error(request, 'Failed to update client.')
    return redirect('core:clients')

@staff_member_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        name = client.name
        client.delete()
        messages.success(request, f'Client "{name}" deleted.')
    return redirect('core:clients')

@staff_member_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully.')
        else:
            messages.error(request, 'Failed to add project. Please check the form.')
    return redirect('core:projects')

@staff_member_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
        else:
            messages.error(request, 'Failed to update project.')
    return redirect('core:projects')

@staff_member_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        title = project.title
        project.delete()
        messages.success(request, f'Project "{title}" deleted.')
    return redirect('core:projects')

# ─── Services CRUD ──────────────────────────────────────────────
@staff_member_required
def services_manager(request):
    all_services = Service.objects.all().order_by('order')
    form = ServiceForm()
    return render(request, 'core/services_manager.html', {
        'active_tab': 'services',
        'services': all_services,
        'form': form,
    })

@staff_member_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully.')
        else:
            messages.error(request, 'Failed to add service.')
    return redirect('core:services_manager')

@staff_member_required
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

@staff_member_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, f'Service "{service.title}" deleted.')
    return redirect('core:services_manager')

# ─── Portfolio CRUD ──────────────────────────────────────────────
@staff_member_required
def portfolio_manager(request):
    items = Project.objects.all().order_by('order')
    form = PortfolioForm()
    return render(request, 'core/portfolio_manager.html', {
        'active_tab': 'portfolio',
        'items': items,
        'form': form,
    })

@staff_member_required
def portfolio_add(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio item added successfully.')
        else:
            messages.error(request, 'Failed to add portfolio item.')
    return redirect('core:portfolio_manager')

@staff_member_required
def portfolio_edit(request, pk):
    item = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio item updated successfully.')
        else:
            messages.error(request, 'Failed to update portfolio item.')
    return redirect('core:portfolio_manager')

@staff_member_required
def portfolio_delete(request, pk):
    item = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        title = item.title
        item.delete()
        messages.success(request, f'Portfolio item "{title}" deleted.')
    return redirect('core:portfolio_manager')

# ─── Testimonials CRUD ──────────────────────────────────────────
@staff_member_required
def testimonials_manager(request):
    all_testimonials = Testimonial.objects.all().order_by('-id')
    form = TestimonialForm()
    return render(request, 'core/testimonials_manager.html', {
        'active_tab': 'testimonials',
        'testimonials': all_testimonials,
        'form': form,
    })

@staff_member_required
def testimonial_add(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial added successfully.')
        else:
            messages.error(request, 'Failed to add testimonial.')
    return redirect('core:testimonials_manager')

@staff_member_required
def testimonial_edit(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully.')
        else:
            messages.error(request, 'Failed to update testimonial.')
    return redirect('core:testimonials_manager')

@staff_member_required
def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        name = testimonial.client_name
        testimonial.delete()
        messages.success(request, f'Testimonial from "{name}" deleted.')

# ─── Contact Messages CRUD ─────────────────────────────────────
@staff_member_required
def messages_inbox(request):
    all_messages = ContactMessage.objects.all().order_by('-created_at')
    unread_count = ContactMessage.objects.filter(is_read=False).count()
    return render(request, 'core/messages_inbox.html', {
        'active_tab': 'messages',
        'contact_messages': all_messages,
        'unread_count': unread_count,
    })

@staff_member_required
def message_toggle_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.is_read = not msg.is_read
        msg.save()
        status = "read" if msg.is_read else "unread"
        messages.success(request, f'Message from {msg.name} marked as {status}.')
    return redirect('core:messages_inbox')

@staff_member_required
def message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        name = msg.name
        msg.delete()
        messages.success(request, f'Message from "{name}" deleted.')
    return redirect('core:messages_inbox')
