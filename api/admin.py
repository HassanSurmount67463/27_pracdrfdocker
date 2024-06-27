from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn", "price", "slug")


admin.site.register(Book, BookAdmin)
