from django.shortcuts import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy

from .models import Board, Column, Task
from accounts.models import Profile


class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'boards'

    def get_queryset(self):
        try:
            username = self.request.session["username"]
            profile = Profile.objects.filter(username=username)[0]
            return profile.board_set.all()
        except KeyError:
            pass


class DetailView(generic.DetailView):
    template_name = 'dashboard/detail.html'
    model = Board


class DeleteView(generic.DeleteView):
    template_name = 'dashboard/delete.html'
    model = Board
    context_object_name = 'board'
    success_url = reverse_lazy('index')


def create_board(request):
    name = request.POST.get('name')
    if name:
        slug = "{}-{}".format(name.lower().replace(' ', '-'), datetime.today())
        description = request.POST.get('description')
        username = request.session["username"]
        profile = Profile.objects.filter(username=username)[0]
        new_board = Board.objects.create(name=name, slug=slug, description=description)
        new_board.owner.add(profile)
        messages.success(request, "New board created!")
    else:
        messages.error(request, "Introduce a name for the new board!")
    return HttpResponseRedirect('/dashboard/')


def create_column(request, pk):
    column_name = request.POST.get('column_name')
    if column_name:
        Column.objects.create(name=column_name, board=Board.objects.filter(pk=pk)[0])
        messages.success(request, "New column created!")
    else:
        messages.error(request, "Introduce a name for the new column!")
    return HttpResponseRedirect(''.join(['/dashboard/', str(pk)]))


def create_task(request, pk, column_id):
    task_description = request.POST.get('task_description')
    task_title = request.POST.get('task_title')
    if all((task_description, task_title)):
        Task.objects.create(column=Column.objects.filter(pk=column_id)[0], title=task_title, description=task_description)
    else:
        messages.error(request, "Introduce a name and a description for the new task!")
    return HttpResponseRedirect(''.join(['/dashboard/', str(pk)]))