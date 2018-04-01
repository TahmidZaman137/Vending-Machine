# ===============================================================================
#
# This script contains all code pertaining to the sound effects used by the app.
#
# ===============================================================================

from kivy.core.audio import SoundLoader
soundPath = r"C:\Users\tahmi\OneDrive\Documents\Git\Vending-Machine\Sounds\\"
successNoise = SoundLoader.load(soundPath + 'chaching.wav')
failureNoise = SoundLoader.load(soundPath + 'breaking.wav')
