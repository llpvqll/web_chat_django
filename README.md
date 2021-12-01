# The web chat was written in django

## To run, you need to set all the requirements:
* Log in to the web_chat_django directory and write to the terminal:
   * ___pip install requirements.txt___
* or
   * ___pip install -r requirements.txt___
  
### After setting the requirements, you need to run the program:
* Log in to the web_chat_django directory and write to the terminal:
   * ___python manage.py runserver___
* or
   * ___py manage.py runserver___
  
#### After starting the server, you can go to the main page where you need to register on the site.
After registration you will be redirected to a page where you can select a chat <br> 
(now you can only select one chat) In the chat you can send a message, after <br>
sending your message will be sent to the server, it will be written to the <br>
postgresql database and returned to the chat. I used __AsynkWebsocketConsumer__ <br>
so there should be no delay in sending the message. <br>
Я також зрозумів можливість відправки відкладеного повідомлення. На сторінці чату <br>
ви можете знайти годинник (під кнопкою відправити), де ви можете встановити час, <br>
і після цього таймер надішле ваше повідомлення.<br>
