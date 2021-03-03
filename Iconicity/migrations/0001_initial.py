# Generated by Django 3.1.7 on 2021-03-03 03:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='inbox', max_length=10)),
                ('author', models.URLField(default='')),
                ('items', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_type', models.CharField(default='author', max_length=10)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('display_name', models.CharField(default='', max_length=30)),
                ('github', models.URLField(default='')),
                ('host', models.URLField(default='')),
                ('url', models.URLField(default='')),
                ('follow', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='post', max_length=10)),
                ('source', models.URLField(default='')),
                ('origin', models.URLField(default='')),
                ('description', models.CharField(default='', max_length=250)),
                ('contentType', models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='', max_length=40)),
                ('content', models.TextField(default='')),
                ('categories', models.JSONField(default=dict)),
                ('count', models.IntegerField(default=0)),
                ('size', models.IntegerField(default=0)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('FRIENDS', 'FRIENDS')], default='PUBLIC', max_length=10)),
                ('unlisted', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeSingle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='Like', max_length=10)),
                ('context', models.URLField(default='')),
                ('summary', models.TextField(default='')),
                ('post_object', models.URLField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iconicity.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Follow', max_length=10)),
                ('summary', models.TextField(default='')),
                ('status', models.CharField(choices=[('sent', 'sent'), ('accepted', 'accepted')], max_length=10)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='Iconicity.userprofile')),
                ('object_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_author', to='Iconicity.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.CharField(default='comment', max_length=10)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField(default='')),
                ('contentType', models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='', max_length=40)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iconicity.userprofile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Iconicity.post')),
            ],
        ),
    ]
