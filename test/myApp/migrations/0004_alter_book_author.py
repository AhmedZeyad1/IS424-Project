# Generated by Django 5.0.6 on 2024-05-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_book_isbn_remove_book_author_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='book', to='myApp.user'),
        ),
    ]
