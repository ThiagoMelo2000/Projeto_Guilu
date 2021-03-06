"""guiluflix URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from web.views import user, lista_de_desejos, novo_adicionamento, update, delete, busca

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', user, name='url_user'),
    path('busca/', busca, name='url_busca'),
    path('lista/', lista_de_desejos, name='url_desejo'),
    path('update/<int:pk>/', update,  name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('novo/', novo_adicionamento, name='url_novo')
]
