
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base),
    path('chat/', include('chat.urls')),
    path('logout/', views.LogoutView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
]
