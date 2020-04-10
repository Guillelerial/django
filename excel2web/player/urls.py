from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.home)  # $ ensures that the path finishes here
]