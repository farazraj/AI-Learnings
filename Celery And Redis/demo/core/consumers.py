import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Group name (all bulk uploads join the same group)
        self.group_name = "bulk_upload_status"

         # Add this socket to the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove socket from group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):

        """
        Optional: if frontend sends messages to server
        """
        # Client messages (if any)
        data = json.loads(text_data)
        print("Received from client:", data)

    async def send_status(self, event):
        """
        Called by Celery tasks via channel_layer.group_send
        """
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
