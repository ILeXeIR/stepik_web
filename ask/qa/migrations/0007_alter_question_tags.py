# Generated by Django 4.1.1 on 2022-10-11 13:04

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('qa', '0006_tag_remove_question_rating_answer_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
    ]
