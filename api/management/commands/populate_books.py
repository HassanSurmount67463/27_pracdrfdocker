# yourapp/management/commands/create_fake_books.py

import decimal

from django.core.management.base import BaseCommand
from faker import Faker

from api.models import Book


class Command(BaseCommand):
    help = "Create fake Book records"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10):  # Adjust the number of books you want to create
            title = fake.sentence(nb_words=3, variable_nb_words=True)
            author = fake.name()
            published_date = fake.date_this_century()
            isbn = fake.isbn13()
            price = decimal.Decimal(
                fake.random_number(digits=3) + "." + fake.random_number(digits=2)
            )

            try:
                book = Book(
                    title=title,
                    author=author,
                    published_date=published_date,
                    isbn=isbn,
                    price=price,
                )
                book.full_clean()
                book.save()
                self.stdout.write(self.style.SUCCESS(f"Created book '{book.title}'"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed to create book: {e}"))
