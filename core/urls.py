from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
