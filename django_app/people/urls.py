from django.conf.urls import url
from . import views

app_name = 'people'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/$', views.add, name='add'),
]