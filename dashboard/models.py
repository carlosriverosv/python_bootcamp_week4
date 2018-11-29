from django.db import models
from django.utils import timezone

from accounts.models import Profile


class Board(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    create_date = models.DateField(default=timezone.now())
    owner = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey(Board, on_delete='cascade')
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}-{}".format(self.board.name, self.name)


class Task(models.Model):
    column = models.ForeignKey(Column, on_delete='cascade')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=280)
    create_date = models.DateField(default=timezone.now())

    def __str__(self):
        return "{}-{}-{}".format(self.column.board.name, self.column.name, self.name)
