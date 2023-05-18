# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:09:35 2021

@author: keerthana
"""

import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("C:/Users/keerthana/Desktop/chat/intents.json",encoding="utf8") as file:
    data = json.load(file)


def chat(inp):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('C:/Users/keerthana/Desktop/chat/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('C:/Users/keerthana/Desktop/chat/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                return np.random.choice(i['responses'])
        