from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        # Add any model-level validation here
        if self.price < 0:
            raise ValidationError("Price cannot be negative")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
