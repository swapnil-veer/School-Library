# Generated by Django 5.0.3 on 2024-03-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='borrow',
            table='borrow',
        ),
    ]