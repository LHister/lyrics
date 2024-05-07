from django.http import JsonResponse
from .reciver import Lyrics

class Home:
    def __init__(self):
        self.instance = ''
    def api(self,request):
        if request.method == 'GET':
            song = request.GET.get('song')
            if song:
                self.instance = Lyrics(song)
        return JsonResponse(
            {
            'Artist': self.instance.get_author(),
            'Title': self.instance.get_title(),
            'Album': self.instance.get_album(),
            'Creation Date': self.instance.get_creation_date(),
            'Lyrics': self.instance.get_lyrics(),
            }
        )


