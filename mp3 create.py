import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import os


fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "testing.mp3"

print('Recording')


audio_data = sd.rec(int(fs*seconds), samplerate = fs, channels=2, dtype = 'int16')
sd.wait()

audio_segment = AudioSegment(
    audio_data.tobytes(),
    frame_rate=fs,
    sample_width=audio_data.dtype.itemsize,
    channels=2
)
current_directory = os.getcwd()
output_path = os.path.join(current_directory, filename)

print('finished recording')
audio_segment.export(filename, format='mp3')
