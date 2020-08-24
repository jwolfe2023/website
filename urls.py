"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from webpages.views import home_view, jungle_view, about_view, main_view
from django.conf.urls import url

urlpatterns = [
    url(r'^admin', admin.site.urls),
#    path(r'^login', include('django.contrib.auth.urls')),
    url(r'^jungle', jungle_view),
    url(r'^about', about_view),
    url(r'^main', main_view),
    url(r'^', home_view, name = 'home'),
]