# Generated by Django 4.2.1 on 2023-05-31 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_pagesread_page_rename_pages_page_numpages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='Chapter',
        ),
    ]