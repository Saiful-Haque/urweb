import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urweb.settings')
django.setup()

from core.models import Service

def populate_services():
    services_data = [
        {
            'title': 'Custom Website Development',
            'description': 'Tailor-made websites built with the latest technologies to ensure performance and scalability.',
            'icon_name': 'code',
            'order': 1
        },
        {
            'title': 'WordPress Solutions',
            'description': 'Expert WordPress development, custom themes, and plugin optimization for your business needs.',
            'icon_name': 'layout',
            'order': 2
        },
        {
            'title': 'E-Commerce Stores',
            'description': 'Powerful online stores with seamless payment integrations and conversion-optimized checkouts.',
            'icon_name': 'shopping-bag',
            'order': 3
        },
        {
            'title': 'UI/UX Design',
            'description': 'User-centric interface designs that prioritize intuitive navigation and high engagement rates.',
            'icon_name': 'pen-tool',
            'order': 4
        },
        {
            'title': 'Website Redesign',
            'description': 'Modernize your outdated site with a fresh look, improved speed, and better accessibility.',
            'icon_name': 'refresh-cw',
            'order': 5
        },
        {
            'title': 'Security & Protection',
            'description': 'Advanced security protocols and monitoring to protect your business and user data.',
            'icon_name': 'shield-check',
            'order': 6
        },
        {
            'title': 'Ongoing Maintenance',
            'description': 'Regular updates, performance monitoring, and daily backups to ensure 99.9% uptime.',
            'icon_name': 'settings',
            'order': 7
        },
        {
            'title': 'Landing Pages',
            'description': 'High-converting landing pages specifically designed for marketing and ad campaigns.',
            'icon_name': 'mouse-pointer-2',
            'order': 8
        }
    ]

    # Clear existing services to ensure a clean state matching the image
    Service.objects.all().delete()
    
    for item in services_data:
        Service.objects.create(**item)
        print(f"Created service: {item['title']}")

if __name__ == '__main__':
    populate_services()
