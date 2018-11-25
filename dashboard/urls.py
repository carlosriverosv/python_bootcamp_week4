from django.urls import path

from .views import IndexView, DetailView, create_board, DeleteView

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('create/', create_board, name='create'),
]