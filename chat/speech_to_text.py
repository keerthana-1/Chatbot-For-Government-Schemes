import speech_recognition as sr 
import threading
import chatbot_response
import time
from gtts import gTTS
from playsound import playsound
import os 



def speech():
    r = sr.Recognizer()
    lang='en'
    while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
        try: 
          
        # use the microphone as source for input. 
            with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
                r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
                audio2 = r.listen(source2) 
                
            # Using google to recognize audio 
                print(lang)
                MyText = r.recognize_google(audio2,language=lang) 
                MyText = MyText.lower() 
                if(MyText=='telugu'):
                    lang='te'
                elif(MyText=='ఇంగ్లీష్'):
                    lang='en'
                print(MyText)
                #ob=chatbot_response.chat(MyText)
                #print(ob)
                
                
                if(MyText=='quit'):
                    break
                playResponce(MyText)
              
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
            
          
        except sr.UnknownValueError: 
            print("no query")
            

def playResponce(responce):
    speak = gTTS(text=responce, lang='en', slow= False)  
    speak.save("captured_voice.mp3")     
    playsound('.\captured_voice.mp3')
    os.remove("captured_voice.mp3")
    
