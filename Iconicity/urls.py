from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.LoginView.as_view(), name = 'login'),
	path('logout', views.logout_view, name = 'logout'),

	path('',views.signup,name = 'signup'),

	# need to fix this part later
	path('friends/like', views.like_view, name="like_post_friend"),
	path('mypost/like', views.like_view, name="like_post_mypost"),
	path('public/like', views.like_view, name="like_post_public"),
	path('following/like', views.like_view, name="like_post_following"),

	path('repost', views.repost, name='repost'),
	path('repost_to_friend', views.repost_to_friend, name='repost_to_friend'),
	path('profile',views.profile,name = "profile"),
	path('mypost', views.mypost, name = 'mypost'),
	path('public',views.mainPagePublic,name = "public"),
	path('friends', views.friends, name = 'friends'),
	path('following',views.following,name = "follow"),
	path('post_form', views.AddPostView.as_view(), name="post_form"),
	path('update_post', views.update_post_view, name='update_post'),
	path('delete',views.delete_post, name = "delete"),
	path('comment_form', views.post_comments, name="comment_form"),

	# Friend Requests functionalities by Shway Wang:
	path('follow_someone', views.follow_someone, name='follow_someone'),
	path('remove_inbox_follow', views.remove_inbox_follow, name='remove_inbox_follow'),
	path('unfollow_someone', views.unfollow_someone, name='unfollow_someone'),
	path('follow_back', views.follow_back, name='follow_back'),
	path('inbox', views.inbox_view, name='inbox'),
	path('send_private_post', views.SendPrivatePostView.as_view(), name='send_private_post'),
	path('all_profiles', views.UserProfileListView.as_view(), name='all_profiles'),
	

	# Unlisted
	path('unlisted/<str:post_id>/', views.unlisted_post, name='unlisted'),
	path('unlisted/<str:post_id>', views.unlisted_post, name='unlisted'),

	# APIs
    path(r'posts/', views.Posts().as_view()),
    path(r'posts', views.Posts().as_view()),
	path(r'author/<str:author_id>/inbox', views.Inboxs().as_view()),
    path(r'author/<str:author_id>/inbox/', views.Inboxs().as_view()),
	path(r'author/<str:author_id>/posts/<str:post_id>/likes', views.Likes().as_view()),
    path(r'author/<str:author_id>/posts/<str:post_id>/likes/', views.Likes().as_view()),

	path(r'author/<str:author_id>/posts/<str:post_id>/comments', views.Comments().as_view()),
    path(r'author/<str:author_id>/posts/<str:post_id>/comments/', views.Comments().as_view()),
	path(r'author/<str:author_id>/posts/<str:post_id>/', views.PostById().as_view()),
    path(r'author/<str:author_id>/posts/<str:post_id>', views.PostById().as_view()),
	path(r'author/<str:author_id>', views.AuthorById().as_view()),
	path(r'author/<str:author_id>/', views.AuthorById().as_view()),
	path(r'author/<str:author_id>/posts/', views.AllPostsByAuthor().as_view()),
	path(r'author/<str:author_id>/posts', views.AllPostsByAuthor().as_view()),
	path(r'author/', views.AllAuthors().as_view()),
	path(r'author', views.AllAuthors().as_view()),
	path(r'author/<str:author_id>/followers/', views.ExternalFollowersByAuthor().as_view()),
    path(r'author/<str:author_id>/followers', views.ExternalFollowersByAuthor().as_view()),
 	#https://iconicity-test-a.herokuapp.com/author/b058b053-4766-4c6a-acaf-561c08badf64/posts/00db788e-45af-49eb-8350-f1c507eb42d0
	path(r'author/<str:author_id>/friendposts/', views.FriendPostsByAuthor().as_view()),
	path(r'author/<str:author_id>/friendposts', views.FriendPostsByAuthor().as_view()),
	# Unlisted
	# path(r'unlisted/<str:post_id>/', views.Unlisted().as_view()),
	# path(r'unlisted/<str:post_id>', views.Unlisted().as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
