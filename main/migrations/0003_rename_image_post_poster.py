# Generated by Django 4.0.5 on 2022-06-16 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='poster',
        ),
    ]
