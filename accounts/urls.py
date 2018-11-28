from django.urls import path
from .views import login, sign_up, log_out

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', log_out, name='logout'),
]