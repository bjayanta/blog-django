# Generated by Django 4.1.1 on 2022-09-17 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_post_media'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
