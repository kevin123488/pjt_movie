# Generated by Django 3.2.12 on 2022-05-20 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communitys', '0002_alter_comment_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='review_title',
        ),
    ]