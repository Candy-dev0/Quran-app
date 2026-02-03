import vlc

class AudioManager:
    def __init__(self):
        # Initialize VLC instance and player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def load_audio(self, file_path):
       #Loads a new audio file into the player.
        media = self.instance.media_new(file_path)
        self.player.set_media(media)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume_level):
        #Expects volume_level between 0 and 100
        self.player.audio_set_volume(int(volume_level))

    def get_time_info(self):

        #Returns current time and total duration in milliseconds.
        #Note: VLC returns -1 if no media is loaded.

        current = self.player.get_time()
        total = self.player.get_length()
        return current, total

    def seek(self, percentage):
        #Jumps to a position in audio
        #EG: 0.0 to 1.0
        self.player.set_position(percentage)