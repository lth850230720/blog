"""blogProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from myBlog import views
from django.conf.urls import url
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index$',views.index),
    url(r'^index/(\d+)',views.index),
    url(r'about',views.about),
    url(r'^divide$',views.divide),
    url(r'^divide/(\w+)/(\d+)',views.divide_blog_menu),
    url(r'^tag$',views.tag),
    url(r'resume',views.resume),
    url(r'^tag/(\w+)/(\d+)',views.tag_blog_menu),
    url(r'test',views.test),
    url(r'blog/(\d+)',views.showBlog),
    url(r'search',views.search)

]
