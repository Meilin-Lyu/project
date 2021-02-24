from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#path('', views.login, name = 'login'),
	path('', views.LoginView.as_view(), name = 'login'),
	path('logout', views.logout_view, name = 'logout'),
	path('signup',views.signup,name = 'signup'),
	path('main', views.main_page, name = 'main_page'),
]