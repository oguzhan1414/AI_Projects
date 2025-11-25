import streamlit as st
from ai_module import generate_blog_intro
st.title("SEO Blog Creator 🚀")

topic = st.text_input("Blog konusu girin:")

if st.button("Blog Girişi Üret"):
    if topic:
        result = generate_blog_intro(topic)
        st.write("### Üretilen Giriş Paragrafı")
        st.write(result)
    else:
        st.warning("Lütfen bir konu girin!")
