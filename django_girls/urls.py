from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_girls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name="about_me"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}), #sobrescribes la url que ya tiene django que importaste en las otras url, para pasarle el parametro de next_page
    #esta de logout hay que ponerla encima de estas de abajo que estamos importando para que la sobreescriba.
    url('^', include('django.contrib.auth.urls')),

]
