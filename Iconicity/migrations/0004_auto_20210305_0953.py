# Generated by Django 3.1.6 on 2021-03-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iconicity', '0003_auto_20210305_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='externalFollows',
            field=models.JSONField(default=dict),
        ),
    ]
