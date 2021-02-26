from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm

from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import logout
from django.http.request import HttpRequest

#https://thecodinginterface.com/blog/django-auth-part1/
# Shway Wang put this here:
# below is put here temperarily, just to display the format
posts = [
    {
        "type":"post",
        # title of a post
        "title":"This is a Post Title",
        # id of the post
        "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e",
        # where did you get this post from?
        "source":"http://lastplaceigotthisfrom.com/posts/yyyyy",
        # where is it actually from
        "origin":"http://whereitcamefrom.com/posts/zzzzz",
        # a brief description of the post
        "description":"This post discusses stuff -- brief",
        # The content type of the post
        # assume either
        # text/markdown -- common mark
        # text/plain -- UTF-8
        # application/base64
        # image/png;base64 # this is an embedded png -- images are POSTS. So you might have a user make 2 posts if a post includes an image!
        # image/jpeg;base64 # this is an embedded jpeg
        # for HTML you will want to strip tags before displaying
        "contentType":"text/plain",
        "content":"This is a test post. This is a test post. This is a test post. This is a test post. This is a test post. This is a test post. This is a test post.",
        # the author has an ID where by authors can be disambiguated
        "author":{
                "type":"author",
            # ID of the Author
            "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            # the home host of the author
            "host":"http://127.0.0.1:5454/",
            # the display name of the author
            "displayName":"Lara Croft",
            # url to the authors profile
            "url":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            # HATEOS url for Github API
            "github": "http://github.com/laracroft"
        },
        # categories this post fits into (a list of strings
        "categories":["web","tutorial"],
        # comments about the post
        # return a maximum number of comments
        # total number of comments for this post
        "count": 1023,
        # page size
        "size": 50,
        # the first page of comments
        "comments":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments",
        # You should return ~ 5 comments per post.
        # should be sorted newest(first) to oldest(last)
        "comments":[
            {
                 "type":"comment",
                 "author":{
                     "type":"author",
                     # ID of the Author (UUID)
                     "id":"http://127.0.0.1:5454/author/1d698d25ff008f7538453c120f581471",
                     # url to the authors information
                     "url":"http://127.0.0.1:5454/author/1d698d25ff008f7538453c120f581471",
                      "host":"http://127.0.0.1:5454/",
                      "displayName":"Greg Johnson",
                      # HATEOS url for Github API
                      "github": "http://github.com/gjohnson"
                 },
                 "comment":"Sick Olde English",
                 "contentType":"text/markdown",
                 # ISO 8601 TIMESTAMP
                 "published":"2015-03-09T13:07:04+00:00",
                 # ID of the Comment (UUID)
                 "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments/f6255bb01c648fe967714d52a89e8e9c",
            }
        ],
        # ISO 8601 TIMESTAMP
        "published":"2015-03-09T13:07:04+00:00",
        # visibility ["PUBLIC","FRIENDS"]
        "visibility":"PUBLIC",
        # for visibility PUBLIC means it is open to the wild web
        # FRIENDS means if we're direct friends I can see the post
        # FRIENDS should've already been sent the post so they don't need this
        "unlisted":False
        # unlisted means it is public if you know the post name -- use this for images, it's so images don't show up in timelines
    }
]

author = {
    "type":"author",
    # ID of the Author
    "id":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
    # the home host of the author
    "host":"http://127.0.0.1:5454/",
    # the display name of the author
    "displayName":"Lara Croft",
    # url to the authors profile
    "url":"http://127.0.0.1:5454/author/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
    # HATEOS url for Github API
    "github": "http://github.com/laracroft"
}

# Create your views here.



def getAuthor(id):
    author_profile = serializers.serialize("json", UserProfile.objects.filter(uid=id))
    jsonload = json.loads(author_profile)[0]
    raw_id = jsonload['pk']
    jsonload = jsonload['fields']
    temp = str(jsonload['host']) + '/author/' + str(raw_id)
    jsonload['user_id'] = str(jsonload['host']) + '/author/' + str(raw_id)
    jsonload['url'] = jsonload['user_id']
    return Response(jsonload)

def postAuthor(id):
    # update author profile
    pass

# not in use at this moment
class AuthorProfile(APIView):
    # get a author's profile by its id
    def get(self, request, id):
        author_profile = serializers.serialize("json", UserProfile.objects.filter(uid=id))
        jsonload = json.loads(author_profile)[0]
        raw_id = jsonload['pk']
        jsonload = jsonload['fields']
        temp = str(jsonload['host']) + '/author/' + str(raw_id)
        jsonload['user_id'] = str(jsonload['host']) + '/author/' + str(raw_id)
        jsonload['url'] = jsonload['user_id']
        return Response(jsonload)
        
# get all followers this author has
# id is the author's id
def getFollowers(id):
    authorfollow = getAuthor(id).data['follow'] # return followe list of this author
    # now it should be a list of urls.

    
    print(type(authorfollow))
    print(authorfollow)
    #print(json.loads(authorfollow))
    
def logout_view(request):
    # in use, support log out
    # http://www.learningaboutelectronics.com/Articles/How-to-create-a-logout-button-in-Django.php
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('login'))
    
    
class LoginView(View):
    def get(self, request):
        return render(request, 'Iconicity/login.html', { 'form':  AuthenticationForm })
    def post(self,request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:
                form.clean()
            except ValidationError:
                return render(
                    request,
                    'Iconicity/login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            login(request, form.get_user())

            return redirect(reverse('main_page'))

        return render(request, 'Iconicity/login.html', { 'form': form })

# citation:https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-profile-model


"""TODO:
Question asked by Qianxi:
for the following two lines:

user = authenticate(username=username, password=raw_password)
login(request, user)

we need exception handling.

Finish it and delete this comment block
"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User = authenticate(username=username, password=raw_password)
            Github = form.cleaned_data.get('github')
            host = request.get_host()
            createUserProfile(username, User, Github, host)

            login(request, User)
            return redirect('main_page')
            
    else:
        form = SignUpForm()
    return render(request, 'Iconicity/signup.html', {'form': form})

@login_required
def main_page(request):
    userProfile = getUserProfile(request.user)

    # get all the posts posted by the current user
    post_object_list = [obj.as_dict() for obj in getPosts(userProfile)]
    
    if len(post_object_list) == 0:
        post_json = None
    else:
        post_json=json.dumps(post_object_list)
    #print("post_json",post_json)
    #print(type(post_json))
    context = {
        'posts': post_json,
        'UserProfile': userProfile
    }

    """Note:
    Consider that there are case when there's no posts of this author
    change main_page.html so that it looks better when there's no post for
    from author.

    finish this and delete this comment block.
    """
    return render(request, 'Iconicity/main_page.html', context)

def createUserProfile(Display_name, User, Github, host):
    profile = UserProfile(user=User, 
                          display_name=Display_name,
                          github=Github,
                          host=host)
    profile.url = str(host) + '/author/' + str(profile.uid)
    profile.save()

def getUserProfile(currentUser):
    # return a UserProfile object for the current login user
    return UserProfile.objects.filter(user=currentUser).first()

def getPosts(userProfile):
    return Post.objects.filter(author=userProfile)
