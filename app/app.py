import streamlit as st
import pandas as pd
import pickle
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense




#from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
import numpy as np


model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(17,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])





try:
    prediction = model.predict(model_input)
    print("Prediction made successfully:", prediction)
except Exception as e:
    print("Could not make a prediction. Error:")

st.title('Fresh water prediction')




ph = st.number_input(label="**Ph**",min_value=1.0,step=0.00000000000000000000000000001,max_value=20.0,value =7.232588,format="%f")

iron = st.number_input(label="**Iron**",min_value=2.047587e-55,step=1.0e-100,max_value=5.0e+2,value =1.388450e-02,format="%e")

nitrate = st.number_input(label="**Nitrate**",min_value=2.861727e-03,step=1.0e-100,max_value=9.639078e+05,value =4.082173e+0,format="%e")

chloride = st.number_input(label="**Chloride**",min_value=2.363919e+0,step=1.0e-100,max_value=1.507310e+04,value =342.375355,format="%e")

lead = st.number_input(label="**Lead**",min_value=0e-0,step=1.0e-1000,max_value=1.507310e+04,value =9.234052e-247,format="%e")

zinc = st.number_input(label="**Zinc**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =0.847062e-0,format="%e")

color = st.number_input(label="**Color**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =3.0e-0,format="%e")

turbidity = st.number_input(label="**Turbidity**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =0.044137e-0,format="%e")

flouride = st.number_input(label="**Flouride**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =1.394104e-0,format="%e")

copper = st.number_input(label="**Copper**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =2.058487e-0,format="%e")

odor = st.number_input(label="**Odor**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =3.855576e-0,format="%e")

sulfate = st.number_input(label="**Sulfate**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =124.028697e-0,format="%e")

conductivity = st.number_input(label="**Conductivity**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =713.070569e-0,format="%e")

chlorine = st.number_input(label="**Chlorine**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =3.688366e-0,format="%e")

magnese = st.number_input(label="**Magnese**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =0.000378e-0,format="%e")

tds = st.number_input(label="**Total dissolved salts**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =4.162845e-0,format="%e")

water_temp = st.number_input(label="**Water temperature**",min_value=0e-0,step=1.0e-100,max_value= 100e+5,value =45.650479e-0,format="%e")


model_input = [ph,iron,nitrate, chloride,lead,zinc,color,turbidity,flouride,copper,odor,sulfate,conductivity,chlorine,magnese,tds,water_temp]


model_input = np.array(model_input)
st.write(len(model_input))

model_input = model_input.reshape(1, -1) 
prediction = model.predict(model_input)

st.write(model.summary())

if prediction >= 0.5:
    st.write("water is drinkable")

if prediction < 0.5:
    st.write("water is drinkable")

# print(prediction)
