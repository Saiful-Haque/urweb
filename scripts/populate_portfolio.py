import os
import django
from django.utils.text import slugify

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urweb.settings')
django.setup()

from core.models import Project

def populate_portfolio():
    projects_data = [
        {
            'title': 'Quantum Pay',
            'category': 'Fintech',
            'technologies': 'React • Node.js',
            'description': 'Next-generation payment gateway for borderless digital transactions.',
            'image_style': 'dark',
            'link': '#',
            'order': 1
        },
        {
            'title': 'SaaSFlow',
            'category': 'SaaS',
            'technologies': 'TypeScript • AWS',
            'description': 'Unified workflow management for remote-first engineering teams.',
            'image_style': 'accent', # Tealish
            'link': '#',
            'order': 2
        },
        {
            'title': 'Luxe Real Estate',
            'category': 'Fintech',
            'technologies': 'Vue • Firebase',
            'description': 'Premium property listings with virtual 3D tour integration.',
            'image_style': 'light',
            'link': '#',
            'order': 3
        },
        {
            'title': 'EcoStore',
            'category': 'E-commerce',
            'technologies': 'Next.js • Shopify',
            'description': 'Sustainable marketplace for conscious lifestyle products.',
            'image_style': 'eco-green', # Light green
            'link': '#',
            'order': 4
        },
        {
            'title': 'HealthTrack',
            'category': 'Healthcare',
            'technologies': 'Flutter • Python',
            'description': 'Personalized health monitoring and predictive analysis app.',
            'image_style': 'health-peach', # Peach
            'link': '#',
            'order': 5
        },
        {
            'title': 'Artisan Hub',
            'category': 'Marketplace',
            'technologies': 'PHP • Laravel',
            'description': 'Connecting local craftsmen with global collectors.',
            'image_style': 'artisan-beige', # Beige
            'link': '#',
            'order': 6
        },
        {
            'title': 'CogniVision',
            'category': 'AI & ML',
            'technologies': 'Python • TensorFlow',
            'description': 'Real-time object detection and spatial analysis for retail.',
            'image_style': 'dark',
            'link': '#',
            'order': 7
        }
    ]

    # Clear existing projects
    Project.objects.all().delete()
    
    for item in projects_data:
        item['slug'] = slugify(item['title'])
        Project.objects.create(**item)
        print(f"Created project: {item['title']}")

if __name__ == '__main__':
    populate_portfolio()
