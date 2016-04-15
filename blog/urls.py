from django.conf.urls import include, url
from .views import Post
from . import views

urlpatterns = [
	url(r'^$', views.post_list.as_view(), name="post_list"),
	#	url(r'^$', views.post_list, name='post_list'), la hemos sustituido por la de arriba que es una class based view
	url(r'^post/new$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #Para definir una variable en las RegExp es con: ?P<nombre de la variable>
	url(r'^post/(?P<pk>[0-9]+)/edit$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete$', views.post_delete, name='post_delete'),	
]