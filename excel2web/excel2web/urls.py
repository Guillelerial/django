"""excel2web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'welcome/', views.welcome_page),
    path(r'player/', include('player.urls')),
    # The above entry chops anything before 'player/' and then looks up the url on the player app
    url(r"^$", views.welcome_page)
]
