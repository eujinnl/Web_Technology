# Generated by Django 4.1.3 on 2023-01-08 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='userid')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('department', models.CharField(max_length=50, verbose_name='department')),
            ],
        ),
    ]