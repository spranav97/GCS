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

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        text_data_json['type']='chat_message'
        if text_data_json['COM']!='1':
            self.v=connect(text_data_json['COM'])

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    # Receive message from room group
    async def chat_message(self, event):
        try:
            data1={
                'roll':self.v.attitude.roll,
                'pitch':self.v.attitude.pitch,
                'yaw':self.v.attitude.yaw,
            }
            # Send message to WebSocket
            await self.send(text_data=json.dumps(data1))
        except:pass
