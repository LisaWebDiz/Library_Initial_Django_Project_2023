from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'publication_date')
    list_editable = ('price', 'exist')
    list_filter = ('exist',)


admin.site.register(Book, BookAdmin)

