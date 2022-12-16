#!/bin/python

import tkinter as tk
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import speech_recognition as sr
import io
from pydub import AudioSegment
from translate import Translator

t = Translator(from_lang="es", to_lang="en")

tokenizer = Wav2Vec2Processor.from_pretrained(
    'jonatasgrosman/wav2vec2-large-xlsr-53-spanish')
model = Wav2Vec2ForCTC.from_pretrained(
    'jonatasgrosman/wav2vec2-large-xlsr-53-spanish')

r = sr.Recognizer()

win = tk.Tk()
# Define a function to print something inside infinite loop
condition = False


def infinite_loop():
    with sr.Microphone(sample_rate=16000) as source:
        if condition:
            audio = r.listen(source)
            data = io.BytesIO(audio.get_wav_data())
            clip = AudioSegment.from_file(data)
            x = torch.FloatTensor(clip.get_array_of_samples())
            inputs = tokenizer(x, sampling_rate=16000,
                               return_tensors='pt', padding='longest').input_values
            logits = model(inputs).logits
            tokens = torch.argmax(logits, axis=-1)
            text = tokenizer.batch_decode(tokens)
            tk.Label(win, text=t.translate(
                str(text).lower()), font="Arial, 25").pack()
            win.after(100, infinite_loop)


def escuchar():
    global condition
    condition = True
    win.after(0, infinite_loop)


def detenerse():
    global condition
    condition = False


# Create a button to escuchar the infinite loop
escuchar = tk.Button(win, text="Escuchar",
                     font="Arial, 12", command=escuchar).pack()
detenerse = tk.Button(win, text="Detenerse",
                      font="Arial, 12", command=detenerse).pack()

# Call the infinite_loop function after 1 sec.
win.after(0, infinite_loop)

win.mainloop()
