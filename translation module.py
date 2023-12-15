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
language_list = [ "These are the available languages: ","French - fr", "Spanish - es", "Japanese - ja", "Ukranian - uk",
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
print(output)
#this is simply the string of translated text language
print(translated)
