import streamlit as st
import gateway

import streamlit as st

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
import streamlit as st

st.set_page_config(
   page_title="Escritor GPT-3",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="collapsed",
)

def header():
    st.header('Resumidor')
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Texto para resumir", height=250)
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])
    
    if colum1.button("Resuma"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_resumidor(txt)
            
            if status == 200:
                st.text_area(label="Texto resumido:", value=new_txt, height=250)
                st.success("¡Resumió!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Resumidor ❄️")
header()
instert_text()
