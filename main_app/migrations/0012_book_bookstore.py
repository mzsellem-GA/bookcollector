# Generated by Django 4.2.1 on 2023-06-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_bookstore_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookstore',
            field=models.ManyToManyField(to='main_app.bookstore'),
        ),
    ]
