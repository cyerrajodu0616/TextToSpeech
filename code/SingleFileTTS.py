import pyttsx3
import datetime

Text_list = [
              '''Adorable Toddler's Hilarious Concern During FaceTime '''
              ,'''My toddler dropped my phone while she was FaceTiming my mom, gasped, picket it back up, and asked   '''
              ,'''"grandma, are you ok???" '''
              , ''' It was cutest, dumbest thing I have ever seen.'''
             ]

i = 0
for text in Text_list:
    engine = pyttsx3.init();


    engine.setProperty("speed",50)
    text_input = text
#engine.say(text_input);
    engine.save_to_file(text_input,f"C:\\Users\\ycrag\\work\\gitHubRepo\\TextToSpeech\\content\\cutest{i}.mp3")
    i+=1

engine.runAndWait() ;
