from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
# in class -> reverse_lazy, in function -> reverse
from django.urls import reverse_lazy



# Create your views here.

class Todolist(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = { 'title','memo','priority','duedate' }
    success_url = reverse_lazy('rlist')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('rlist')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = { 'title','memo','priority','duedate' }
    success_url = reverse_lazy('rlist')
