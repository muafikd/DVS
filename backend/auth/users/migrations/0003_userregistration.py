# Generated by Django 4.2.7 on 2023-12-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_isadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12, unique=True)),
                ('metamask_address', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
