from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import json
from .models import Group,Chat


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        groupname = self.scope['url_route']['kwargs']['groupname']
        print("websocket connected",event)
        async_to_sync(self.channel_layer.group_add)(groupname,self.channel_name) # add channel to a group
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self, event):
        print("websocket message recieved",event['text'])
        self.user = self.scope["user"]
        # for i in range(10):
        #     self.send({
        #         'type': 'websocket.send',
        #         'text': 'messege from server ' + str(i),
        #     })
        #     sleep(1)

        if self.scope['user'].is_authenticated:
            groupname = self.scope['url_route']['kwargs']['groupname']
            data = json.loads(event['text'])
            group = Group.objects.get(name=groupname)
            chat = Chat(
                user= self.user,
                content = data.get('msg'),
                group = group
            )
            chat.save()
            data['user'] = self.scope['user'].username
            async_to_sync(self.channel_layer.group_send)(groupname, {
                'type': 'chat.message',
                'message': json.dumps(data)})
        else:
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({"msg": "Login Required","user": "unknown"})
            })
        
    def chat_message(self, event): 
        print("Event...",event)
        self.send({
                    'type': 'websocket.send',
                    'text': event['message']
                })

    def websocket_disconnect(self, event):
        print("websocket disconnected",event)
        groupname = self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_discard)("groupname", self.channel_name)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connected", event)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("websocket message recieved", event)

    async def websocket_disconnect(self, event):
        print("websocket disconnected", event)
