# Generated by Django 4.2.13 on 2024-06-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanelapp', '0003_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
