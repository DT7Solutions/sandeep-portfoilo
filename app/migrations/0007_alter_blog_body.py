# Generated by Django 5.0.6 on 2024-05-15 12:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]