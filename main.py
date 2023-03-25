import streamlit as st
from EditDistance import *
from ReadData import *

word_pool = create_word_pool()

# Streamlit app
st.title("Did you spell it right?")

# user input field
user_input = st.text_area("Start Typing..", key="userinput")

words = user_input.split()  # Split the string into words
# last_word = words[-1]

updated_string = ""

for word in words:
    closest_word = get_minimum_edit_distance_word(word, word_pool)

    updated_string += " " + closest_word

st.text("Corrected Text:")
st.text(updated_string)
