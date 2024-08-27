import streamlit as st
import pandas as pd

st.title("🎈 My new app")
#st.write(
#  "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

choice = st.selectbox("Chart Type:", ["", "line", "bar"])

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

if (choice == "bar"):
  st.bar_chart(df)
elif (choice == "line"):
  st.line_chart(df)
