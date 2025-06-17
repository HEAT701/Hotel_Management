from django.urls import path
from.import views

urlpatterns = [
  path("Hotels/",views.List_Hotel, name="List_Hotel"),
]
