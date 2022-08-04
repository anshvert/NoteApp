from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getroutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getnotes(request):

    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getnote(request,pk):

    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many=False)

    return Response(serializer.data)


@api_view(['POST',"GET"])
def createnote(request):

    data = request.data
    note = Note.objects.create(
        body = data['body']
    )

    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatenote(request,pk):

    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletenote(request,pk):

    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Note was deleted!')

