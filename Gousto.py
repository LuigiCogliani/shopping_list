import streamlit as st
import pandas as pd


st.write("""# Gousto Grocery List Generator""")

df = pd.read_csv('df.csv')

filter = st.sidebar.multiselect('Choose recipies',df['name'].unique()) 
df_ = df[df['name'].isin(filter)]
df_ = df_.groupby('ing_name', as_index=False)['ing_q'].sum()

text = df_.to_string(header=False,index=False,justify='left')

for line in text.splitlines():
        st.checkbox(line)



