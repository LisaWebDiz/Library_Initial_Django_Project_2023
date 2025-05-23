from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from books.serializer import BookSerializer


class BooksApiTestCase(APITestCase):
    def test_get_list(self):
        book_1 = Book.objects.create(title='Книга_1', price=511, pages_quantity=250)
        book_2 = Book.objects.create(title='Книга_2', price=1099, pages_quantity=500)

        response = self.client.get(reverse('books_api_list'))

        serial_data = BookSerializer([book_1, book_2], many=True).data
        serial_data = {'books_list': serial_data}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)
