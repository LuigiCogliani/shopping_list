import streamlit as st
import pandas as pd
import smtplib

st.write("""# Gousto Grocery List Generator""")

df = pd.read_csv('df.csv')

st.sidebar.multiselect('Choose recipies',df['name'].unique()) 

df_ = df.groupby('ing_name', as_index=False)['ing_q'].sum()

st.write(df_)

text = df_.to_string(header=False,index=False,justify='left')
st.write(type(text))
text = 'Shopping List\n' + text

def send_email():
    sender_email = 'stevio.bar@gmail.com'
    rec_email = 'house.cogliani@gmail.com'
    password = 'Luigifox7'
    message = text

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email,password)
    server.ehlo()
    server.sendmail(sender_email,rec_email,message)

st.button('Send!',on_click=send_email)