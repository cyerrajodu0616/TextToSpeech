import pyttsx3;
engine = pyttsx3.init();
engine.setProperty("speed",150)
text_input = 'If you want to see the goodness of someone, then take advice from him.'
engine.say(text_input);
engine.save_to_file(text_input,"text_input.mp3");

engine.runAndWait() ;