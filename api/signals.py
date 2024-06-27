import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Book

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Book)
def log_book_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f'A new book "{instance.title}" has been created.')
    else:
        logger.info(f'The book "{instance.title}" has been updated.')
