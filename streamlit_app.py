import streamlit
import requests
import pandas
import snowflake.connector

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Frühstücksfavoriten')
streamlit.text('🥣 Omega 3 & Heidelbeer-Haferflocken')
streamlit.text('🥗 Smoothie mit Grünkohl, Spinat und Rucola')
streamlit.text('🐔 Hartgekochtes Freilandei')
streamlit.text('🥑🍞 Avocado-Toast')

streamlit.header('🍌🥭 Bau deinen eigenen Frucht-Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

fruityvice_normalized = pandas.json_normalized(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

