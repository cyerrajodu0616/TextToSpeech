from gtts import gTTS
text_input = 'They can spend days without any human interaction with ease. They feel bad for your poor sense of humour but try to laugh to make you happy. Knowing the answer but still not answering in class. When placing an order if they cant pronounce the name properly then that dish would not be ordered. Ask the youger sibling to do things so that you dont have to leave the house. Every conversation has a pre-existing script inside their head. They are actually quite funny and hilarious inside their head and wish that people knew about it. They dont indulge in conversation with others because they are busy having a debate inside their head. They are really funny and witty over texts but calls are awkward for them. They are quite conscious about their personality.'
tts = gTTS(text_input)
tts.save('hello.mp3')