# Generated by Django 4.2.7 on 2024-01-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_details', '0006_alter_borrowmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowmodel',
            name='title',
            field=models.CharField(default='Nothing', max_length=30),
        ),
    ]
