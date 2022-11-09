import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Mom\'s New Helathy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avocado Toast')

streamlit.header('🍌🍓Build your own Smoothie🥝🍇')
# Display the table on the page.
streamlit.text('Fruits to pick!')
# streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.text('Fruits picked!')
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

import request

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


