# Generated by Django 5.0.6 on 2024-05-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Form_type',
            field=models.CharField(choices=[('contact', 'contact'), ('invite', 'invite')], default='contact', max_length=30),
        ),
    ]
