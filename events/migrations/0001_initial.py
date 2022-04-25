# Generated by Django 4.0.3 on 2022-04-25 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('contact_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Posted')),
            ],
        ),
    ]
