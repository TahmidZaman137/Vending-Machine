#===============================================================================
#
# This script contains all code pertaining to the sound effects used by the app.
#
#===============================================================================

from kivy.core.audio import SoundLoader
successNoise = SoundLoader.load('chaching.wav')
failureNoise = SoundLoader.load('breaking.wav')