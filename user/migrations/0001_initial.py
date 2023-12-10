# Generated by Django 3.1.8 on 2023-12-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
