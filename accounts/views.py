import requests
from django.shortcuts import render
from django.template import loader
from requests.exceptions import ConnectionError
from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile


def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            response = requests.post("http://localhost:5000/users/auth/", json={"email": email, "password": password})
            if response.status_code == 200:
                response = response.json()
                request.session["username"] = response.get("data", {}).get("username")
                return HttpResponseRedirect('/dashboard/')
            else:
                response = response.json()
                context["message"] = response.get("error", {}).get("description")
                template = loader.get_template('home/index.html')
                return HttpResponse(template.render(context, request))
        except ConnectionError:
            context["message"] = "Unable to connect :("
            template = loader.get_template('home/index.html')
            return HttpResponse(template.render(context, request))


def sign_up(request):
    if request.method == "GET":
        return render(request, 'home/signup.html')
    elif request.method == "POST":
        context = {}
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            response = requests.post("http://localhost:5000/users/",
                                     json={"email": email, "username": username, "password": password})
            if response.status_code == 201:
                response = response.json()
                username = response.get("data", {}).get("username")
                request.session["username"] = username
                Profile.objects.create(username=username)
                return HttpResponseRedirect('/dashboard/')
            else:
                response = response.json()
                context["message"] = response.get("error", {}).get("description")
                template = loader.get_template('home/signup.html')
                return HttpResponse(template.render(context, request))
        except ConnectionError:
            context["message"] = "Unable to connect :("
            template = loader.get_template('home/signup.html')
            return HttpResponse(template.render(context, request))


def log_out(request):
    if request.method == "GET":
        try:
            del request.session["username"]
        except KeyError:
            pass
        return HttpResponseRedirect('/')
