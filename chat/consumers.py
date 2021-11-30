import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
import datetime
from time import sleep


class ChatRoomConsumer(AsyncWebsocketConsumer):
    # connection with chatroom
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # set group name and channel name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    # disconnect method
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def set_info(self):
        return Message.objects.create(author=self.username,
                                      content=self.message)

    # take info from chat
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.message = text_data_json['message']
        self.username = text_data_json['username']

        date = datetime.datetime.now()
        send_time = ''
        self.send_time = text_data_json['send_time']
        now = (str(date.hour) + ':' + str(date.minute))

        if self.send_time == '':
            self.add_to_db = await database_sync_to_async(self.set_info)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chatroom_message',
                    'message': self.message,
                    'username': self.username,
                }
            )
        elif self.send_time == now:
            self.add_to_db = await database_sync_to_async(self.set_info)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chatroom_message',
                    'message': self.message,
                    'username': self.username,
                }
            )
        else:
            now_hour = date.hour
            now_minute = date.minute
            send_hour, send_minute = self.send_time.split(':')
            if now_hour != send_hour:
                if now_minute != send_minute:
                    timer = ((int(send_hour) - int(now_hour)) * 3600) + ((int(send_minute) - int(now_minute)) * 60)
                    sleep(timer)
                else:
                    timer = (int(send_hour) - int(now_hour)) * 3600
                    sleep(timer)
            else:
                timer = (int(send_minute) - int(now_minute)) * 60
                sleep(timer)

            self.add_to_db = await database_sync_to_async(self.set_info)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chatroom_message',
                    'message': self.message,
                    'username': self.username,
                }
            )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))



