#!/usr/bin/env bash

declare -a text="The quick brown fox jumps over the lazy dog"

declare -a tts_models=(
    "tts_models/en/ljspeech/fast_pitch"
    "tts_models/en/ljspeech/glow-tts"
    "tts_models/en/ljspeech/speedy-speech"
    "tts_models/en/ljspeech/tacotron2-DDC_ph"
)

declare -a vocoder_models=(
    "vocoder_models/en/ljspeech/hifigan_v2"
    "vocoder_models/en/ljspeech/multiband-melgan"
    "vocoder_models/en/ljspeech/multiband-melgan"
    "vocoder_models/en/ljspeech/univnet"
    "vocoder_models/universal/libri-tts/fullband-melgan"
)

for model_name in "${tts_models[@]}"
do
    for vocoder_name in "${vocoder_models[@]}"
    do
        tts --text "${text}" --model_name "${model_name}" --vocoder_name "${vocoder_name}" --out_path "${model_name//\//-}-${vocoder_name//\//-}".wav
    done
done