from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('tags/', views.TagsListView.as_view(), name="tags-list-view"),
]

app_name = "to_do_list"
