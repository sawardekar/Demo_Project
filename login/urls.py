from django.conf.urls import patterns, url
from login import views

# urlpatterns = [
#     url(r'^$', views.index,name='index'),
# ]

urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    url(r'^register/$', views.register_list, name='register_list'),
    url(r'^register/new$', views.register_create, name='register_new'),
    url(r'^register/edit/(?P<pk>\d+)$', views.register_update, name='register_edit'),
    url(r'^register/delete/(?P<pk>\d+)$', views.register_delete, name='register_delete'),
]
