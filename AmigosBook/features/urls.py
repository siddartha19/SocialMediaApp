from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^login/$', views.userAuth, name ="user authencation"),
     url(r'^signup/$', views.registerUser, name ="user register"),
     url(r'^newpost/$', views.createPost, name ="Create post"),
     url(r'^likepost/$', views.likePost, name ="Like post"),
     url(r'^commentpost/$', views.commentPost, name ="Comment post"),
     url(r'^posts/$', views.listPosts, name ="List posts"),
]