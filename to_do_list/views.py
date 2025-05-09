from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View

from to_do_list.forms import TaskForm
from to_do_list.models import Tag, Task
from django.urls import reverse_lazy

class IndexView(generic.View):
    model = Task
    template_name = "to_do_list/index.html"
    context_object_name = "tasks"

    def get(self, request):
        tasks = Task.objects.all().order_by('is_done', '-created_at')
        return render(request, self.template_name, {'tasks': tasks})

    def post(self, request):
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, pk=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect('to_do_list:index')

class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "to_do_list/tags_list.html"

class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:index")

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:tags-list-view")

class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do_list/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do_list:tags-list-view")

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:index")

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:index")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_list/task_confirm_delete.html"
    success_url = reverse_lazy("to_do_list:index")

