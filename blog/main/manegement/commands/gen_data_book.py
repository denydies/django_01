import random
#
# from django.core.management.base import BaseCommand
from django.core.management import BaseCommand
from faker import Faker
from main.models import Author, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(50):
            Author(name=fake.name(), email=fake.email(), age=random.randint(1, 100)).save()

        for i in range(100):
            author = Author.objects.order_by('?').last()
            Book(title=f'title{i}', author=author).save()
