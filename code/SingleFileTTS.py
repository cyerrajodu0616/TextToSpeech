import pyttsx3
import datetime

Text_list_Female = [
               '''Leaving Walmart, Halfway home. Why sweetiee?'''
              , ''' OH DARN!! Be there in a Bit..'''
             ]

Text_list_Male = [
              '''Mom, Where are You???'''
              , ''' You brought me to walmart with you!!'''
             ]

i = 0

engine = pyttsx3.init()
engine.setProperty("speed",50)
voices = engine.getProperty('voices')

for v in voices:
    print(v)

for text in Text_list_Male:
    engine.setProperty("voice", voices[0].id)
    text_input = text
#engine.say(text_input);
    engine.save_to_file(text_input,f"C:\\Users\\ycrag\\work\\gitHubRepo\\TextToSpeech\\content\\shopping_Male_{i}.mp3")
    i+=1


for text in Text_list_Female:
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty("voice", voices[1].id)
    text_input = text
#engine.say(text_input);
    engine.save_to_file(text_input,f"C:\\Users\\ycrag\\work\\gitHubRepo\\TextToSpeech\\content\\shopping_Female_{i}.mp3")
    i+=1

engine.runAndWait()
