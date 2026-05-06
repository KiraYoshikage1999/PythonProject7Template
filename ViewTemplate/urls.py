from django.contrib import admin
from . import views
from django.urls import path , include

urlpatterns = [
    path('', views.index, name="start_page"),
    path('style/', views.style, name="style_page"),
    path('contacts/', views.contacts, name="contacts_page")
    # path("", views.index, name="index"),
    # path("football/", views.football, name="football"),
    # path("hockey/", views.hockey, name="hockey"),
    # path("basketball/", views.basketball, name="basketball"),
    # path( "text-format/", views.text_format, name="text-format"),
    # path("recipes/<recipe:str>/", views.goulash, name="goulash"),
    # path("recipes/<recipe:str>/", views.dumplings, name="dumplings"),
]