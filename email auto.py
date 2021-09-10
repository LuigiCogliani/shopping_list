import streamlit as st
import pandas as pd
import smtplib

st.write("""# Gousto Grocery List Generator""")

df = pd.read_csv('df.csv')

filter = st.sidebar.multiselect('Choose recipies',df['name'].unique()) 
df_ = df[df['name'].isin(filter)]
df_ = df_.groupby('ing_name', as_index=False)['ing_q'].sum()

text = df_.to_string(header=False,index=False,justify='left')


#yandex mail settings
#https://www.lifewire.com/what-are-the-yandex-mail-smtp-settings-1171304
# def send_email(text):
    
#     rec_email = 'house.cogliani@gmail.com'
#     message = text

#     sender_email = 'stevio.bar@gmail.com'
#     password = 'Luigifox7'
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     #server.ehlo()
#     server.starttls()
#     server.login(sender_email,password)
#     #server.ehlo()
#     server.sendmail(sender_email,rec_email,message)
#     # sender_email = 'hosue.cogliani@yandex.com'
#     # password = 'B0tcogliani!'
#     # server = smtplib.SMTP('smtp.yandex.com', 465)
#     # server.login(sender_email,password)
#     # server.sendmail(sender_email,rec_email,message)
def shopping_list():
    for line in text.splitlines():
        st.checkbox(line)

if st.button('Generate!'):
    shopping_list()


