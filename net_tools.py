import os
import requests
import constants


def download_surah(surah_num, reciter_name, save_path):
    """
    Downloads a surah based on the reciter's display name and surah number.
    Uses the slug mapping from constants.py to build the URL.
    """
    # 1. Get the technical slug from the human-readable name
    # Example: "Mishary Rashid Alafasy" -> "mishaari_raashid_al_3afaasee"
    reciter_slug = constants.RECITERS.get(reciter_name)

    if not reciter_slug:
        print(f"Error: Reciter '{reciter_name}' not found in constants.")
        return False

    # 2. Format surah number to 3 digits (001, 002, etc.)
    surah_str = str(surah_num).zfill(3)

    # 3. Build the URL using the base URL and the slug
    url = f"{constants.BASE_URL}{reciter_slug}/{surah_str}.mp3"

    # 4. Ensure the directory exists before saving
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    try:
        print(f"Downloading: {url}")
        # Using stream=True for better memory management with large audio files
        response = requests.get(url, stream=True, timeout=15)

        if response.status_code == 200:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Successfully saved to: {save_path}")
            return True
        else:
            print(f"Failed! HTTP Status: {response.status_code}")
            return False

    except Exception as e:
        print(f"Connection Error: {e}")
        return False