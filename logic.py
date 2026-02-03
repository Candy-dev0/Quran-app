import os
import constants
import net_tools
from audio_manager import AudioManager

# 1. Initialize the player once at the top level
player = AudioManager()


def play_request(surah_num, reciter):
    # Ensure surah_num is 3 digits (e.g., "1" -> "001") for the file path
    formatted_surah = str(surah_num).zfill(3)


    path = os.path.join(constants.base_folder, reciter, f"{formatted_surah}.mp3")

    if os.path.exists(path):
        print(f"Playing local file: {path}")
        player.load_audio(path)
        player.play()
    else:
        print(f"Downloading {formatted_surah} for {reciter}...")

        success = net_tools.download_surah(surah_num, reciter, path)

        if success:
            player.load_audio(path)
            player.play()
        else:
            print("Download failed. Check internet connection.")


def seek(percentage):
    player.seek(percentage)
def set_volume(percentage):
    player.set_volume(percentage)


def format_time(ms):

    if ms < 0:
        return "00:00"

    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)

    return f"{minutes:02d}:{seconds:02d}"