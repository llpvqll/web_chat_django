from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from . models import Message
from .forms import MessageForm, UserCreateForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        if request.user.is_authenticated:
            message = Message.objects.all()
            context = {
                'message': message,
                'message_form': MessageForm,
            }
            return render(request, self.template_name, context)
        else:
            context = {}
            return render(request, self.template_name, context)
