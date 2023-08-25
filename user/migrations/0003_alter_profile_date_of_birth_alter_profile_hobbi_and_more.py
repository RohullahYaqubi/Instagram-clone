# Generated by Django 4.2.4 on 2023-08-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobbi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='live_in',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupassion',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
