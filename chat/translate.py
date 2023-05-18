from googletrans import Translator 
from gtts import gTTS
from playsound import playsound
import os 
from langdetect import detect

translator = Translator()
translation = translator.translate('Quit' , dest='te')
print(translation.text)
#print(detect("నేను బాగున్నాను"))
text = translation.text
speak = gTTS(text=text, lang='te', slow= False)  
speak.save("captured_voice.mp3")     
playsound('.\captured_voice.mp3')
os.remove("captured_voice.mp3")