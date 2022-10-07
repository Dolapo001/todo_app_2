from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = (
        "title",
        "body",
    )
    template_name = "task_edit.html"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("article_list")


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

