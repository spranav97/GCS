from channels.generic.websocket import AsyncWebsocketConsumer
import json
from dronekit import connect

class ConnectConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'connect'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        try:
            self.v.close()
            print('Flight Controller Connection Terminated')
            #send message to all other users that FC is disconnected
        except:pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['COM']!='1':
            self.v=connect(text_data_json['COM'])
        try:
            data1={
                'type':'chat_message',
                'roll':self.v.attitude.roll,
                'pitch':self.v.attitude.pitch,
                'yaw':self.v.attitude.yaw,
            }
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                data1
            )
        except:pass

    # Receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
