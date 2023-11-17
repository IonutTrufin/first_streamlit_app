import streamlit
import pandas

streamlit.title('New healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🐔Eggs and bacon')
streamlit.text('🍞 Bread, butter and apricot jam')
streamlit.text('🥣 🥗 🐔 🥑 Some other stuff')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

