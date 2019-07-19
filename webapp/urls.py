from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
import re



urlpatterns = [
    path('users/', views.userList.as_view()),
    path('hello/<int:pk>/', views.userDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)