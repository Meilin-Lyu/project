from .models import *
from .config import *
from rest_framework import serializers as rest_serializers
from django.contrib.auth.models import User
import datetime
from urllib import request
import json



class FollowersSerializer(rest_serializers.ModelSerializer):
    items = rest_serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ('items',)

    def get_items(self, obj):
        return obj.get_followers()

# https://www.django-rest-framework.org
class PostSerializer(rest_serializers.ModelSerializer):
    post_id = rest_serializers.SerializerMethodField()
    id = rest_serializers.SerializerMethodField()
    author = rest_serializers.SerializerMethodField()
    count = rest_serializers.SerializerMethodField()
    size = rest_serializers.SerializerMethodField()
    like_count = rest_serializers.SerializerMethodField()
    source = rest_serializers.SerializerMethodField()
    origin = rest_serializers.SerializerMethodField()
    contentType = rest_serializers.SerializerMethodField()
    description = rest_serializers.SerializerMethodField()
    comments = rest_serializers.SerializerMethodField()
    author_display_name = rest_serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('post_id', 'id', 'title', 'type', 'source', 'origin', 'description', 'contentType',
        'author', 'content', 'visibility', 'categories', 'unlisted','image','like','external_likes',
        'count', 'size', 'published', 'author', 'host','like_count','comments', 'author_display_name')

    def get_author_display_name(self, obj):
        return UserProfile.objects.filter(user=obj.author).first().displayName

    def get_comments(self, obj):
        url = obj.origin
        if obj.source != "" and obj.source != None:
            url = obj.source
        comments = []
        try:
            comments = Comment.objects.filter(post=url)

        except Exception as e:
            print("Exception in post comments")
            return []

        else:
            serializer_data = CommentSerializer(list(comments),many=True).data
            return serializer_data

    def get_post_id(self, obj):
        return obj.post_id

    def get_id(self, obj):
        return obj.id

    def get_author(self, obj):
        return GETProfileSerializer(UserProfile.objects.filter(user=obj.author).first()).data

    def get_like_count(self, obj):
        return obj.count_like()

    def get_count(self, obj):
        return obj.count

    def get_size(self, obj):
        return obj.size

    def get_source(self, obj):
        return str(obj.source)

    def get_origin(self, obj):
        return str(obj.origin)

    def get_contentType(self, obj):
        return obj.contentType

    def get_description(self,obj):
        if len(obj.content)>50:
            return obj.content[:50]
        else:
            return obj.content

class CommentSerializer(rest_serializers.ModelSerializer):
    type = rest_serializers.SerializerMethodField("get_type")
    id = rest_serializers.SerializerMethodField()
    author = rest_serializers.SerializerMethodField()
    published = rest_serializers.SerializerMethodField()
    contentType = rest_serializers.SerializerMethodField()
    comment = rest_serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('type', 'author','published','contentType','comment','id')
 
    def get_type(self, obj):
        return obj.type

    def get_author(self, obj):
        return obj.author
        
    def get_published(self, obj):
        return obj.published

    def get_contentType(self, obj):
        return obj.contentType

    def get_comment(self, obj):
        return obj.comment

    def get_id(self, obj):
        return obj.id
        

class GETProfileSerializer(rest_serializers.ModelSerializer):
    type = rest_serializers.SerializerMethodField("get_type")
    id = rest_serializers.SerializerMethodField("get_id")
    displayName = rest_serializers.SerializerMethodField("get_name")
    host = rest_serializers.SerializerMethodField()
    github = rest_serializers.SerializerMethodField()
    url = rest_serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ('type', 'id', 'url', 'host', 'displayName','github')

    def get_type(self, obj):
        return obj.type

    def get_id(self, obj):
        return obj.url

    def get_name(self, obj):
        return obj.displayName

    def get_host(self, obj):
        return obj.host

    def get_github(self, obj):
        return obj.github

    def get_url(self,obj):
        return obj.url

class LikeSerializer(rest_serializers.ModelSerializer):
    context = rest_serializers.SerializerMethodField()
    summary = rest_serializers.SerializerMethodField()
    author = rest_serializers.SerializerMethodField()
    object = rest_serializers.SerializerMethodField()
    type = rest_serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ('context','summary','author','object','type')

    def get_context(self,obj):
        return obj.context
    
    def get_summary(self, obj):
        return obj.summary

    def get_object(self,obj):
        return obj.object

    def get_author(self,obj):
        return obj.author

    def get_type(self,obj):
        return obj.type

class InboxSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ('items','author','type')

# By: Shway Wang, the serializer for FriendRequest
class FriendRequestSerializer(rest_serializers.ModelSerializer):
    type = rest_serializers.SerializerMethodField()
    summary = rest_serializers.SerializerMethodField()
    actor = rest_serializers.SerializerMethodField()
    object = rest_serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = ('type', 'summary', 'actor', 'object')
    
    def get_type(self, obj):
        return obj.type

    def get_summary(self, obj):
        return obj.summary

    def get_actor(self, obj):
        return obj.actor

    def get_object(self, obj):
        return obj.object
