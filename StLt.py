# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:59:30 2024

@author: vikas
"""
import speech_recognition as sr
import pyaudio

import streamlit as st


st.image('images/how to celebrate birthday of a children/Image_1.jpg', caption='1')

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
 
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)
        st.write(text)
else:
    st.write('Goodbye')
    
    