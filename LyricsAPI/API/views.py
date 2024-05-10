from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .reciver import Lyrics  

class Home(APIView):
    def get(self, request):
        song = request.GET.get('song')
        if len(song) < 1:
            return Response({'error': 'Please provide a song name'}, status=400)
        if not song:
            return Response({'error': 'Please provide a song name'}, status=400)
        try:
            lyrics_instance = Lyrics(song)
            song_info = {
                'Artist': lyrics_instance.get_author(),
                'Title': lyrics_instance.get_title(),
                'Album': lyrics_instance.get_album(),
                'CreationDate': lyrics_instance.get_creation_date(),
                'Lyrics': lyrics_instance.get_lyrics(),
            }
            return Response(song_info)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
