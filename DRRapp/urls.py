from django.contrib import admin
from django.urls import path
from DRRapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("updateOrUpdate", views.updateOrUpdate, name='updateOrUpdate'),
    path("nextpage/<int:showAmount>/<int:fromEntry>/<int:toEntry>", views.nextPage, name='nextPage'),
    path("previuspage/<int:showAmount>/<int:fromEntry>/<int:toEntry>", views.previusPage, name='previusPage'),
]
