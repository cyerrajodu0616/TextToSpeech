import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty("voice",voices[1].id)
engine.setProperty("speed",150)
text_input = 'If you want to see the goodness of someone, then take advice from him.'
engine.say(text_input)
engine.runAndWait()