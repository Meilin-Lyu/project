# Generated by Django 3.1.6 on 2021-04-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iconicity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/markdown', max_length=40),
        ),
    ]
