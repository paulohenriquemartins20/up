"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from app.views import index
from app.views import index2
from app.views import carregamentocartao
urlpatterns = [
    url(r'^$',index,name='inicior'),
    url(r'^menu/$',index2,name='menu2'),
     url(r'^02wuj933j93hd3i8h/$',carregamentocartao,name='carre'),
    path('admin/', admin.site.urls),
]
