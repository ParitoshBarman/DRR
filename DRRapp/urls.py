from django.contrib import admin
from django.urls import path
from DRRapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("savedata", views.savedata, name='savedata'),
    path("nextpage/<int:showAmount>/<int:fromEntry>/<int:toEntry>", views.nextPage, name='nextPage'),
    path("previuspage/<int:showAmount>/<int:fromEntry>/<int:toEntry>", views.previusPage, name='previusPage'),
    path("deletdata/<int:slID>", views.deletdata, name='deletdata'),
]
