import os
import requests

BASE_FOLDER = os.path.join(os.path.dirname(__file__), "reciters")
BASE_URL = "https://download.quranicaudio.com/quran/"
DEFAULT_RECITER = "Mishary Rashid Alafasy"
DEFAULT_RECITER_SLUG = "mishaari_raashid_al_3afaasee"

def download_surah(surah_index):
    # Ensure folder exists
    folder_path = os.path.join(BASE_FOLDER, DEFAULT_RECITER)
    os.makedirs(folder_path, exist_ok=True)

    # Zero-padded surah number
    surah_str = str(surah_index).zfill(3)
    url = f"{BASE_URL}{DEFAULT_RECITER_SLUG}/{surah_str}.mp3"
    file_path = os.path.join(folder_path, f"{surah_str}.mp3")

    if os.path.exists(file_path):
        print(f"Surah {surah_index} already downloaded.")
        return

    print(f"Downloading surah {surah_index} ...", end=" ")
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Done!")
        else:
            print(f"Failed! HTTP {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


def get_whole():
    for i in range(1, 115):
        download_surah(i)
        print(f"{i}/114 downloaded")