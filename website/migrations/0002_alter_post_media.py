# Generated by Django 4.1.1 on 2022-09-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(upload_to='assets/images'),
        ),
    ]
