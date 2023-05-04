import pyaudio
import wave


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 5
filename = "testing.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
from pydub import AudioSegment
sound = AudioSegment.from_wav('testing.wav')

sound.export('testing.mp3', format='mp3')
import os
os.remove('testing.wav')

#Speech-to-text module
import os
from google.cloud import speech
#json file insert
client = speech.SpeechClient.from_service_account_file('.json')

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
#json file insert
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'.json'

translate_client = translate_v2.Client()

#language list for each language
language_list = [ "These are the available lanuages: ","French - fr", "Spanish - es", "Japanese - ja", "Ukranian - uk",
                 "Portuguese(brazil) - pt-BR", "German - de", "Chinese(PRC) - zn-CN",
                 "Thai - th", "Italian - it"]

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

#Text-to-speech module
import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1
#json file insert
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.json'
client = texttospeech_v1.TextToSpeechClient()

text = translated

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
