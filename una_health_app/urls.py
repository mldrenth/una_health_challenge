from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("/<int:value_id>/", views.show_value_by_id, name="show_value_by_id")
   
]
    
