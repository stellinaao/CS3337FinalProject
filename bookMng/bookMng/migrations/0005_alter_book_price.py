# Generated by Django 4.1.3 on 2022-11-17 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
