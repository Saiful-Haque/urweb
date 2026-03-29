from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('about/', views.about_view, name='about'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/clients/', views.clients_view, name='clients'),
    path('dashboard/projects/', views.projects_view, name='projects'),
    path('dashboard/add-client/', views.add_client, name='add_client'),
    path('dashboard/clients/<int:pk>/edit/', views.edit_client, name='edit_client'),
    path('dashboard/clients/<int:pk>/delete/', views.delete_client, name='delete_client'),
    path('dashboard/add-project/', views.add_project, name='add_project'),
    path('dashboard/projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('dashboard/projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('dashboard/services/', views.services_manager, name='services_manager'),
    path('dashboard/services/add/', views.service_add, name='service_add'),
    path('dashboard/services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('dashboard/services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('dashboard/portfolio/', views.portfolio_manager, name='portfolio_manager'),
    path('dashboard/portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('dashboard/portfolio/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
    path('dashboard/portfolio/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('dashboard/testimonials/', views.testimonials_manager, name='testimonials_manager'),
    path('dashboard/testimonials/add/', views.testimonial_add, name='testimonial_add'),
    path('dashboard/testimonials/<int:pk>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('dashboard/testimonials/<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),
    path('dashboard/messages/', views.messages_inbox, name='messages_inbox'),
    path('dashboard/messages/<int:pk>/toggle-read/', views.message_toggle_read, name='message_toggle_read'),
    path('dashboard/messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('dashboard/messages/send/', views.send_email, name='send_email'),
    path('dashboard/messages/<int:pk>/reply/', views.send_email, name='reply_to_message'),
]
