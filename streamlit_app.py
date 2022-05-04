import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Frühstücksfavoriten')
streamlit.text('🥣 Omega 3 & Heidelbeer-Haferflocken')
streamlit.text('🥗 Smoothie mit Grünkohl, Spinat und Rucola')
streamlit.text('🐔 Hartgekochtes Freilandei')
streamlit.text('🥑🍞 Avocado-Toast')

streamlit.header('🍌🥭 Bau deinen eigenen Frucht-Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

