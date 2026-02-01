# Quran app prototype for PC:

## Project goal:
My aim with this project is to make a functional free and ad free quran app which allows for quran playback on any device.

## Current project state:
It is currently in Prototype phase and only has a CLI to interact with it but I plan to include a GUI later into development. It is currently based on Python for Proof of Concept and easier development but I plan to switch to JavaScript later on in development. It currently only allows Mishary Rashid Alafasy as the default reciter but I plan to add more reciters as an option in this program.

## Roadmap:
I plan to make a prototype v2 after I get feedback on this version and I plan to include a UI with it as well.

## How it works:

### Initializing:
Use the following commands before in your python terminal:
``` 
pip install requests
```
```
pip install audioplayer
```
OR
```
pip install -r requirements.txt
```
in the quran app directory
### How to use:
Put both files **audio_manager.py** and **net_tools.py** in the same folder and open **"audio_manager.py"** select a surah numbered from 1-114 from the list printed above the program will automatically download that specific surah and play it, it will also ask you that do you want to get all the surahs recited by that reciter.

## Credits:
`https://quranicaudio.com/` for the quran surahs mp3 files.
