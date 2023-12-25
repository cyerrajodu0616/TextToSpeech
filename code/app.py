import TTS

text="The quick brown fox jumps over the lazy dog"

tts_models=["tts_models/en/ek1/tacotron2","tts_models/en/ljspeech/tacotron2-DDC","tts_models/en/ljspeech/tacotron2-DDC_ph","tts_models/en/ljspeech/glow-tts","tts_models/en/ljspeech/speedy-speech","tts_models/en/ljspeech/tacotron2-DCA","tts_models/en/ljspeech/vits","tts_models/en/ljspeech/vits--neon","tts_models/en/ljspeech/fast_pitch","tts_models/en/ljspeech/overflow","tts_models/en/ljspeech/neural_hmm","tts_models/en/vctk/vits","tts_models/en/vctk/fast_pitch","tts_models/en/sam/tacotron-DDC","tts_models/en/blizzard2013/capacitron-t2-c50","tts_models/en/blizzard2013/capacitron-t2-c150_v2","tts_models/en/multi-dataset/tortoise-v2","tts_models/en/jenny/jenny"]

vocoder_models=["vocoder_models/universal/libri-tts/wavegrad","vocoder_models/universal/libri-tts/fullband-melgan","vocoder_models/en/ek1/wavegrad","vocoder_models/en/ljspeech/multiband-melgan","vocoder_models/en/ljspeech/hifigan_v2","vocoder_models/en/ljspeech/univnet","vocoder_models/en/blizzard2013/hifigan_v2","vocoder_models/en/vctk/hifigan_v2","vocoder_models/en/sam/hifigan_v2","vocoder_models/nl/mai/parallel-wavegan","vocoder_models/code/thorsten/wavegrad","vocoder_models/code/thorsten/fullband-melgan","vocoder_models/code/thorsten/hifigan_v1","vocoder_models/ja/kokoro/hifigan_v1","vocoder_models/uk/mai/multiband-melgan","vocoder_models/tr/common-voice/hifigan"]

with open("../config/Output.txt", "w") as text_file:
    
    for model_name in tts_models:
        for vocoder_name in vocoder_models:
            model = "_".join(model_name.split("/"))
            vocoder = "_".join(vocoder_name.split("/"))
            x = f'tts --text "{text}" --model_name "{model_name}" --vocoder_name "{vocoder_name}" --out_path C:\Work\GitHubRepo\TextToSpeech\{model}-{vocoder}.wav \n'
            text_file.write(x)
