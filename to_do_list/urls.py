from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tags/", views.TagsListView.as_view(), name="tags-list-view"),
    path("tag/create", views.TagCreateView.as_view(), name="tag-create-view"),
    path("tag/<int:pk>/update", views.TagUpdateView.as_view(), name="tag-update-view"),
    path("tag/<int:pk>/delete", views.TagDeleteView.as_view(), name="tag-delete-view"),
    path("task/create", views.TaskCreateView.as_view(), name="task-create-view"),
    path("task/<int:pk>/update", views.TaskUpdateView.as_view(), name="task-update-view"),
    path("task/<int:pk>/delete", views.TaskDeleteView.as_view(), name="task-delete-view"),
    path("task/<int:pk>/toggle", views.toggle_task_status, name="task-toggle-view"),
]

app_name = "to_do_list"
