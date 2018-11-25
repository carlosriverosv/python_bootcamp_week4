from django.shortcuts import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from datetime import datetime
from django.urls import reverse_lazy

from .models import Board


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
    success_url = reverse_lazy('index')


def create_board(request):
    name = request.POST.get('name', None)
    slug = "{}-{}".format(name.lower().replace(' ', '-'), datetime.today())
    new_board = Board.objects.create(name=name, slug=slug)
    messages.add_message(request, messages.INFO, "New board created!")
    return HttpResponseRedirect('/dashboard/')




