import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Carrera

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        carreras = await self.getCarreras()
        data = [{'name': c.name, 'description': c.description} for c in carreras]

        await self.send(text_data=json.dumps({
            "message": data
        }))

    async def disconnect(self, close_code):
        print(f"WebSocket cerrado con código: {close_code}")

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            try:
                data = json.loads(text_data)
                name = data.get("name", "").strip()
                description = data.get("description", "").strip()

                if name and description:
                    await self.guardarCarrera(name, description)
                    await self.send(text_data=json.dumps({"status": "Carrera guardada"}))
                else:
                    await self.send(text_data=json.dumps({"error": "Datos inválidos"}))

            except json.JSONDecodeError:
                await self.send(text_data=json.dumps({"error": "Formato JSON incorrecto"}))

    @database_sync_to_async
    def guardarCarrera(self, name, description):
        return Carrera.objects.create(name=name, description=description)

    @database_sync_to_async
    def getCarreras(self):
        return list(Carrera.objects.all().order_by('name'))
