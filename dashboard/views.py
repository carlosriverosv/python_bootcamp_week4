from django.shortcuts import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy

from .models import Board, Column, Task


class IndexView(generic.ListView):
    model = Board
    template_name = 'dashboard/index.html'
    context_object_name = 'boards'


class DetailView(generic.DetailView):
    template_name = 'dashboard/detail.html'
    model = Board


class DeleteView(generic.DeleteView):
    template_name = 'dashboard/delete.html'
    model = Board
    context_object_name = 'board'
    success_url = reverse_lazy('index')


def create_board(request):
    name = request.POST.get('name', None)
    slug = "{}-{}".format(name.lower().replace(' ', '-'), datetime.today())
    description = request.POST.get('description')
    new_board = Board.objects.create(name=name, slug=slug, description=description)
    messages.add_message(request, messages.INFO, "New board created!")
    return HttpResponseRedirect('/dashboard/')


def create_column(request, pk):
    column_name = request.POST.get('column_name')
    new_column = Column.objects.create(name=column_name, board=Board.objects.filter(pk=pk)[0])
    messages.add_message(request, messages.INFO, "New column created!")
    return HttpResponseRedirect(''.join(['/dashboard/', str(pk)]))


def create_task(request, pk, column_id):
    task_description = request.POST.get('task_description')
    task_title = request.POST.get('task_title')
    new_task = Task.objects.create(column=Column.objects.filter(pk=column_id)[0], title=task_title, description=task_description)
    return HttpResponseRedirect(''.join(['/dashboard/', str(pk)]))
