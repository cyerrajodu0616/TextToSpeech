import pyttsx3
import datetime


Text_list = [ '''This family emergency '''
             ,''''I once called 911 because I cut my finger and wanted to talk to my mom who was a dispatcher '''
             ,''' I called crying and asking to talk to her by name. She was more pissed at my dad for not waking up when I tried to go to him first.'''
             ]

i = 0
for text in Text_list:
    engine = pyttsx3.init();


    engine.setProperty("speed",100)
    text_input = text
#engine.say(text_input);
    engine.save_to_file(text_input,f"Family_Emer_{i}.mp3")
    i+=1

engine.runAndWait() ;
