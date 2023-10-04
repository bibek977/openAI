import openai
from api_key import api_key

openai.api_key = api_key

audio_file = open("sample_audio.mp3",'rb')
transcript = openai.Audio.transcribe('whisper-1',audio_file)
print(transcript)