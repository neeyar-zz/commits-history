# Generated by Django 2.2.13 on 2020-10-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='owner_login',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]