from django.shortcuts import render
from django.views import generic, View
from to_do_list.models import Tag


class IndexView(generic.TemplateView):
    template_name = "to_do_list/index.html"


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "task_list"
    template_name = "to_do_list/tags_list.html"