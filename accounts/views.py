import requests
from django.template import loader
from requests.exceptions import ConnectionError
from django.http import HttpResponse, HttpResponseRedirect


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
    pass