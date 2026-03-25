from django.core.management.base import BaseCommand
from core.models import Service, Project, Testimonial

class Command(BaseCommand):
    help = 'Populates the database with initial content for URWEB'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Service.objects.all().delete()
        Project.objects.all().delete()
        Testimonial.objects.all().delete()

        # Add Services
        services_data = [
            {'title': 'Web Development', 'description': 'Custom-coded solutions built with modern frameworks like Next.js and Tailwind CSS.', 'icon_name': 'code-2', 'order': 1},
            {'title': 'E-Commerce', 'description': 'Scalable online stores with seamless checkout experiences and inventory management.', 'icon_name': 'shopping-cart', 'order': 2},
            {'title': 'Business Sites', 'description': 'Professional digital presence designed to establish authority and generate B2B leads.', 'icon_name': 'layout', 'order': 3},
            {'title': 'Landing Pages', 'description': 'High-converting single pages optimized for your ad campaigns and social media traffic.', 'icon_name': 'zap', 'order': 4},
            {'title': 'Maintenance', 'description': '24/7 technical support, regular security updates, and performance monitoring.', 'icon_name': 'settings', 'order': 5},
        ]
        for item in services_data:
            Service.objects.create(**item)

        # Add Projects
        projects_data = [
            {'title': 'Nexus Wallet Landing', 'category': 'Fintech', 'image_style': 'dark', 'order': 1},
            {'title': 'Aurora Home Decor', 'category': 'E-Commerce', 'image_style': 'light', 'order': 2},
            {'title': 'Voyager SaaS Platform', 'category': 'SaaS Platform', 'image_style': 'accent', 'order': 3},
        ]
        for item in projects_data:
            Project.objects.create(**item)

        # Add Testimonials
        testimonials_data = [
            {'client_name': 'Sarah Jenkins', 'client_title': 'CEO at BOLT', 'avatar_initials': 'SJ', 'quote': 'URWEB transformed our online presence. Our conversion rates increased by 40% within the first month of launching the new site.'},
            {'client_name': 'David Chen', 'client_title': 'Founder of NEXUS', 'avatar_initials': 'DC', 'quote': 'The performance is unbelievable. Our Lighthouse score went up after we switched teams. Truly professional service.'},
            {'client_name': 'Emily Roberts', 'client_title': 'Marketing Director', 'avatar_initials': 'ER', 'quote': 'Great design, fast communication, and a final product that exceeded our expectations. Highly recommend URWEB for any scale project.'},
        ]
        for item in testimonials_data:
            Testimonial.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully populated URWEB database!'))
