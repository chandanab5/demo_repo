#from django.conf.urls import url
from usersapp import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^api/users$',views.user_list),
    re_path(r'^api/users/(?P<pk>[0-9]+)$',views.user_details),
    #re_path(r'^api/validate$', views.validate_user)
]