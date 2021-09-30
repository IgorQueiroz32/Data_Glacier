import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import RobustScaler, MinMaxScaler, LabelEncoder

# loading the trained model
pickle_in = open('model/model_classification.pkl', 'rb')
classifier = pickle.load(pickle_in)





# front end elements of the web page


# display the front end aspect

st.text("Author: Igor Queiroz - Data Scientist")

data =pd.DataFrame(columns=['Region'])

# defining Region
Region = st.selectbox('Region', ('West', 'Midwest', 'South', 'Other/Unknown', 'Northeast'))

if Region == 'Midwest':
    data['Region'] = 0

elif Region == 'Northeast':
    data['Region'] = 1

elif Region == 'Other/Unknown':
    data['Region'] = 2

elif Region == 'South':
    data['Region'] = 3

elif Region == 'West':
    data['Region'] = 4