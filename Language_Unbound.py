import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import os
os.chdir('/home/langunbound/Desktop/translate_project')
import sys
import os
import pyfiglet
def print_big_text(message):
    font = pyfiglet.Figlet()
    ascii_art = font.renderText(message)
    print(ascii_art)

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    print_big_text("Welcome to Language Unbound!")
    fs = 44100  # Record at 44100 samples per second
seconds = 5
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


#Speech-to-text module
import os
from google.cloud import speech

client = speech.SpeechClient.from_service_account_file('key.json')
media_file = "testing.mp3"

with open(media_file, 'rb') as f:
    mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)

    config = speech.RecognitionConfig(
sample_rate_hertz=44000,
enable_automatic_punctuation=True,
language_code='en-US'

    )
response=client.recognize(
    config=config,
    audio=audio_file
)
transcript = response.results[0].alternatives[0].transcript
#this is transcript of speech string only
print("This is your input: ")
print(transcript)
#this is confidence levels and transcript as well
#print (response)

#Translation module
import os
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'

translate_client = translate_v2.Client()

#language list for each language
language_list = [ "These are the available lanuages: ","Arabic - ar", "French - fr", "Japanese - ja", "Ukranian - uk",
                 "Portuguese(brazil) - pt", "German - de", "Chinese(Simplified) - zh", "Hungarian - hu", "Indonesian - id",
                 "Thai - th", "Italian - it", "Polish - pl", "Russian - ru", "Hebrew - he"]


# print each string in the list
for lang in language_list:
   print(lang)

code = input('which langauge would you like to translate to?')
text = transcript
target = code
output = translate_client.translate(
    text,
    target_language=target
)
translated = output['translatedText']
print("This is your translation result: ")
#output is google translated text+ input and langauge
#print(output)
#this is simply the string of translated text language
print(translated)
#dsiplay (translated)

#Text-to-speech module
import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
client = texttospeech_v1.TextToSpeechClient()

text = translated

synthesis_input = texttospeech_v1.SynthesisInput(text=text)
voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code=code,
    ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE
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
user_input = input("Do you want to restart the program? (yes/no): ").lower()

if user_input == "yes" or user_input == "y":
        restart_program()
else:
        print("Exiting the program.")
