# Generated by Django 4.2.1 on 2023-05-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='toolong',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('NR', 'Not Really')], default=('NR', 'Not Really')),
        ),
    ]