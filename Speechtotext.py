#Speech-to-text module
import os
from google.cloud import speech

client = speech.SpeechClient.from_service_account_file('liquid-polygon-379822-24711e8eb8fa.json')

media_file = "demo audio.mp3"

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
print(response)
