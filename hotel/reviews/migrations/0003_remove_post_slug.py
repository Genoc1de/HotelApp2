# Generated by Django 4.1.3 on 2022-11-24 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_post_alter_comment_post_delete_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
