# Generated by Django 5.1.6 on 2025-02-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='contacts/')),
            ],
        ),
    ]
