from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [

    path('waaracomplete/<int:pk>', views.complete,name="comp"),

]
