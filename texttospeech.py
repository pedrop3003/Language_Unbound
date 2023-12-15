#Text-to-speech module
import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
client = texttospeech_v1.TextToSpeechClient()

text = 'Criando um arquivo MP3.'
code = input('which language would you like to translate to?')
synthesis_input = texttospeech_v1.SynthesisInput(text=text)
voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code=code,
    ssml_gender=texttospeech_v1.SsmlVoiceGender.NEUTRAL
)


audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)


with open('output.mp3', 'wb') as output:
  output.write(response.audio_content)
  
from pydub import AudioSegment
from pydub.playback import play

# define the path to the MP3 file
mp3_file = "output.mp3"

# load the MP3 file into an AudioSegment object
audio = AudioSegment.from_file(mp3_file, format="mp3")

# play the audio
play(audio)
