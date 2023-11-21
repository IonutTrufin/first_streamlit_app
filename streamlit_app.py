import streamlit
import pandas



streamlit.title('New healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🐔Eggs and bacon')
streamlit.text('🍞 Bread, butter and apricot jam')
streamlit.text('🥣 🥗 🐔 🥑 Some other stuff')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


# normalize json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# show normalized response in data frame
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_row)



streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thank you for adding ', fruit_choice)

my_cur.execute("Insert into fruit_load_list values ('from streamlit')")
