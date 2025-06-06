# Generated by Django 5.2.1 on 2025-05-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='Книга', max_length=120, null=True, verbose_name='Наименование'),
        ),
    ]
