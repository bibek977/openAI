import openai
from api_key import api_key

openai.api_key = api_key

# audio_file = open("onlineVoice.mp3",'rb')
# audio_file = open("DineshTesting.mp3",'rb')
audio_file = open("dineshIntension.mp3",'rb')
# transcript = openai.Audio.translate('whisper-1',audio_file)
transcript = openai.Audio.translate('whisper-1',audio_file)
print(transcript)