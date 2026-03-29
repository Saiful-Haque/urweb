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
    path('dashboard/add-project/', views.add_project, name='add_project'),
]
