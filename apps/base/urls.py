from django.urls import path
from .views import *
urlpatterns = [
    path('',NewsListAPI.as_view(),name='NewsListAPI'),
    path('create/',NewsCreateAPI.as_view(),name='NewsCreateAPI'),
    path('update/<int:pk>/',NewsUpdateAPI.as_view(),name='NewsUpdateAPI'),
    path('delete/<int:pk>/',NewsDeleteAPI.as_view(),name='NewsDeleteAPI'),
    path('<int:pk>/',NewsRetrieveAPI.as_view(),name='NewsRetrieveAPI'),




    path('list_create/', SettingsListCreateAPI.as_view(), name="settings create and list api"),
    path('multi/<int:pk>/', SettingsMultiAPI.as_view(), name="settings multi api"),

]