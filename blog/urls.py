from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from .views import Post
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name="post_list"),
    #   url(r'^$', views.post_list, name='post_list'), la hemos sustituido por la de arriba que es una class based view
    url(r'^post/new$', views.PostCreate.as_view(), name='post_new'),
    #   url(r'^post/new$', login_required(views.PostCreate.as_view(), login_url='login'), name='post_new'), #forma alternativa a crear el mixin
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'), #Para definir una variable en las RegExp es con: ?P<nombre de la variable>
    url(r'^post/(?P<pk>[0-9]+)/edit$', views.PostEdit.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^comment/(?P<pk>[0-9]+)/like$', views.comment_like, name='comment_like'),
    url(r'^comment/(?P<pk>[0-9]+)/dislike$', views.comment_dislike, name='comment_dislike'),
]