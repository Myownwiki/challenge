from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
import re



urlpatterns = [
    path('hello/users/', views.userList.as_view()),
    #path('hello/<int:pk>/', views.userDetail.as_view()),
    #path('hello/(?P<username>\w+)/$', views.userDetail),
    url(r'^hello/(?P<username>\w+)/$', 
                       views.userDetail,
                       name='userDetails'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)