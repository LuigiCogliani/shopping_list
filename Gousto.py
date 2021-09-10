import streamlit as st
import pandas as pd
import smtplib

def send_email(text):
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



st.write("""# Gousto Grocery List Generator""")

df = pd.read_csv('df.csv')

filter = st.sidebar.multiselect('Choose recipies',df['name'].unique()) 
df_ = df[df['name'].isin(filter)]
df_ = df.groupby('ing_name', as_index=False)['ing_q'].sum()

text = df_.to_string(header=False,index=False,justify='left')
text = 'Shopping List\n' + text

st.button('Send!',on_click=send_email(text))
st.write(df_)



