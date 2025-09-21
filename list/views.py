from django.http import (
    HttpResponseRedirect,
    HttpRequest
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import (
    generic,
    View
)

from list.forms import (
    TaskForm,
    TagForm
)
from list.models import (
    Task,
    Tag
)


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.all().prefetch_related("tags")


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:tag-list")


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class ChangeStatusView(View):
    def post(
        self,
        request: HttpRequest,
        pk=int
    ) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        redirect_url = request.POST.get(
            "next",
            reverse_lazy("list:task-list")
        )
        return HttpResponseRedirect(redirect_url)
