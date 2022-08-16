from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    #food/
    path("show/",views.IndexView.as_view(),name="index"),

    #food/id/
    path("<int:pk>",views.DetailView.as_view(),name="detail"),
    #add/
    path("add/",views.AddItem.as_view(),name="add_item"),
    # edit
    path("edit/<int:id>/",views.edit_item,name="edit_item"),
    #delete
    path("delete/<int:id>/",views.delete,name="delete"),
]
