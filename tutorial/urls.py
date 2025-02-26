"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import HomePageView, AboutPageView, index
from .views import CarreraCreateViewPage, CarrerasEditarPageView, CarrerasEliminarPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('index/', index, name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('carrera/crear', CarreraCreateViewPage.as_view(), name="carrera/crear"),
    path("carreras/editar/<int:pk>", CarrerasEditarPageView.as_view(), name="editar_carrera"),
    path('carreras/eliminar/<int:pk>', CarrerasEliminarPageView.as_view(), name="eliminar_carrera")
]