import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from .data_loader import get_answer
from .tasks import raise_support_ticket

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket CONNECTED")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        user_msg = text_data.strip().lower()
        print(user_msg)

        async def answer_logic():
            answer = get_answer(user_msg)
            return answer

        try:
            answer = await asyncio.wait_for(answer_logic(), timeout=10.0)

            if answer:
                await self.send(text_data=answer)
            else:
                await self.send(text_data="Let me check with our team...")
                raise_support_ticket.delay(user_msg)
        except asyncio.TimeoutError:
            await self.send(text_data="No response found. A support ticket has been raised.")
            raise_support_ticket.delay(user_msg)