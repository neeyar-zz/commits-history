# Generated by Django 2.2.13 on 2020-10-23 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
    ]
