from audioplayer import AudioPlayer as Player
import os
from net_tools import download_surah
# Default reciter
default_reciter = "Mishary Rashid Alafasy"

# List of all 114 surahs
listsurah = [
    "Al-Fatihah", "Al-Baqarah", "Ali 'Imran", "An-Nisa'", "Al-Ma'idah",
    "Al-An'am", "Al-A'raf", "Al-Anfal", "At-Tawbah", "Yunus",
    "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr",
    "An-Nahl", "Al-Isra'", "Al-Kahf", "Maryam", "Ta-Ha",
    "Al-Anbiya'", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan",
    "Ash-Shu'ara'", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum",
    "Luqman", "As-Sajdah", "Al-Ahzab", "Saba'", "Fatir",
    "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
    "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiyah",
    "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
    "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman",
    "Al-Waqi'ah", "Al-Hadid", "Al-Mujadilah", "Al-Hashr", "Al-Mumtahanah",
    "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Taghabun", "At-Talaq",
    "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij",
    "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah",
    "Al-Insan", "Al-Mursalat", "An-Naba'", "An-Nazi'at", "'Abasa",
    "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
    "At-Tariq", "Al-A'la", "Al-Ghashiyah", "Al-Fajr", "Al-Balad",
    "Ash-Shams", "Al-Layl", "Ad-Duha", "Ash-Sharh", "At-Tin",
    "Al-'Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-'Adiyat",
    "Al-Qari'ah", "At-Takathur", "Al-'Asr", "Al-Humazah", "Al-Fil",
    "Quraysh", "Al-Ma'un", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
    "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"
]

# Base folder where reciter files are stored
base_folder = os.path.join(os.path.dirname(__file__), "reciters")


def get_file_path(reciter, surah_index):

    surah_number = surah_index + 1
    folder = os.path.join(base_folder, reciter)
    file_name = f"{surah_number:03d}.mp3"  # zero-pad 3 digits
    return os.path.join(folder, file_name)


def play_surah(surah_index, reciter=default_reciter):

    file_path = get_file_path(reciter, surah_index)

    # Download if missing
    if not os.path.exists(file_path):
        print(f"Surah {surah_index + 1} not found locally. Downloading...")
        download_surah(surah_index + 1)

    # Play the surah
    if os.path.exists(file_path):
        player = Player(file_path)
        player.play(block=True)
    else:
        print(f"File not found even after download attempt: {file_path}")


def choose_surah():

    # Display surah list
    for i, name in enumerate(listsurah):
        print(f"{i + 1}. {name}")

    # User selects one surah
    try:
        number = int(input("Choose a surah number (1-114): ")) - 1
        if 0 <= number < len(listsurah):
            play_surah(number)
        else:
            print("Invalid surah number!")
    except ValueError:
        print("Please enter a valid number.")

    # Ask if they want to grab all surahs of the current reciter
    grab_all = input(f"\nDo you want to grab all surahs recited by {default_reciter}? (yes/no): ").lower()
    if grab_all == "yes":
        print(f"Downloading all surahs for {default_reciter}...")
        for i in range(114):
            file_path = get_file_path(default_reciter, i)
            if not os.path.exists(file_path):
                print(f"Downloading surah {i + 1}/114 ...", end=" ")
                download_surah(i + 1)
                print("Done!")
        print("All surahs downloaded.")
    else:
        print("Okay, not downloading the full library.")


# For testing standalone
if __name__ == "__main__":
    choose_surah()
