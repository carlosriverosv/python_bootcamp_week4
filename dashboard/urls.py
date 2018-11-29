from django.urls import path

from .views import IndexView, DetailView, create_board, DeleteView, create_column, create_task

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('create/', create_board, name='create'),
    path('<int:pk>/column/', create_column, name='create_column'),
    path('<int:pk>/column/<int:column_id>/task/', create_task, name='create_task'),
]
