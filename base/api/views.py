from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import roomserializer

@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getrooms(request):
    rooms = Room.objects.all()
    serializer = roomserializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getroom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = roomserializer(room, many=False)
    return Response(serializer.data)