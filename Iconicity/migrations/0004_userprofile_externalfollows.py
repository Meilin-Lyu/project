# Generated by Django 3.1.6 on 2021-03-04 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iconicity', '0003_auto_20210303_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='externalFollows',
            field=models.JSONField(default=dict),
        ),
    ]
