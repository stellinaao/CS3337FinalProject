# Generated by Django 4.1.3 on 2022-11-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0005_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_ratings',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
    ]
