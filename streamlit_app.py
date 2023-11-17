import streamlit
import pandas

streamlit.title('New healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🐔Eggs and bacon')
streamlit.text('🍞 Bread, butter and apricot jam')
streamlit.text('🥣 🥗 🐔 🥑 Some other stuff')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

