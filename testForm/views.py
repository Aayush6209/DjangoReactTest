from django.shortcuts import render

# Create your views here.
from .models import User
import json

# SuperUser
# user, kites@123

def index(request):
    var = User.objects.all()
    # print(var)
    # print(type(var))
    # users_json= json.load(User.objects.all())
    return render(request, "testForm/index.html", {
        "users": User.objects.all(),
        # "users_json": users_json
    })


def addUser(request):
    if request.method == "POST":
        name = request.POST["name"]
        newUser = User(name=name)
        newUser.save()
    return index(request)
