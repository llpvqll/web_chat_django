from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Message
from django.core.paginator import Paginator


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        return HttpResponseRedirect('/')


def get_message():
    message = Message.objects.all()
    content = []
    for item in message:
        content.append(to_json(item))
    return content


def to_json(message):
    return {
        'content': message.content,
        'author': message.author,
        'time': str(message.time),
    }


def room(request, room_name):
    if request.user.is_authenticated:
        message = get_message()
        return render(request, 'chatroom.html', {
            'room_name': room_name,
            'message': message,
        })
    else:
        return HttpResponseRedirect('/')


