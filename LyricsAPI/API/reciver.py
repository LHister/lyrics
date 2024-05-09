import lyricsgenius

class Lyrics:
    def __init__(self,song):
        self.actoken =  '0bvxWg2D-WNzv4siSsX2NBvIv-USbPZo1w22Qw26SxjREOHfwgTMdpcyJ0jPDdto'
        self.genius = lyricsgenius.Genius(self.actoken)
        self.song = self.genius.search_song(song,get_full_info=True)
    
    def get_author(self):
        if self.song:
            return self.song.artist
        return "Song not found."

    def get_album(self):
        if self.song:
            return self.song.album if hasattr(self.song, 'album') else "Unknown"
        return "Song not found."

    def get_lyrics(self):
        if self.song:
            return self.song.lyrics
        return "Song not found."
    
    def get_title(self):
        if self.song:
            return self.song.title
        return "Song not found."
        
    def get_creation_date(self):
        if self.song:
            return self.song.year if hasattr(self.song, 'year') else "Unknown"
        return "Song not found."


