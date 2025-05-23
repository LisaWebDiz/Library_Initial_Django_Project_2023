from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=120, default='Книга', null=True, verbose_name='Наименование')
    description = models.TextField(blank=True, null=False, verbose_name='Описание')
    pages_quantity = models.IntegerField(null=False, verbose_name='Количество страниц')
    price = models.FloatField(default=500, null=True, verbose_name='Цена')
    cover_type = models.CharField(max_length=30, null=False, verbose_name='Тип обложки')
    size = models.CharField(max_length=120, null=False, verbose_name='Размер',)
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    exist = models.BooleanField(default=True, null=True, verbose_name='В каталоге?')

    def __str__(self):
        return 'Книга: ' + self.title

    def get_absolute_url(self):
        return reverse('the_book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
