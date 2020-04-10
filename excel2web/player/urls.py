from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    url(r'home', views.home, name="player_home"),  # $ ensures that the path finishes here
    url(r'login$', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    url(r'logout$', LogoutView.as_view(), name="player_logout"),
    url(r'new_invitation$', views.new_invitation, name="player_new_invitation")
]