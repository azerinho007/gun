from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("",views.first,name="index"),
    path("cnn",views.cnn,name="cnn"),
    path("rnn",views.rnn,name="rnn"),
    path("crnn",views.crnn,name="crnn"),
    path("work",views.work, name="work")
]
