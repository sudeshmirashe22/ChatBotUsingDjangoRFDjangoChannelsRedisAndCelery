from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index_new(request):
    return render(request, 'room1.html')

# def index(request):

#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         User.objects.create(username=username, email=email)

#         return redirect('chat_room', username, email)

# def chat_room(request, username, email):

#     User.objects.get(username = username)

#     context ={
#         'username' : username,
#         'email' : email
#     }

#     return render(request, 'room.html', context)