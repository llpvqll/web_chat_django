from django.db import models
# Create your models here.


class Message(models.Model):
    author = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.time}:{self.author}:{self.content}'


