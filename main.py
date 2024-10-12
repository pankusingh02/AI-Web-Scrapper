import streamlit as st
from scrape import scrape_website
from scrape import(
    scrape_website,
    clean_body_content,
    split_dom_content,
    extract_body_content
)

from parse import parse_with_ollama

st.title("AI web Scraper")
url= st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the Website")


    result= scrape_website(url)
    body_content=extract_body_content(result)
    cleaned_content= clean_body_content(result)

    st.session_state.dom_content = cleaned_content

    with st.expander("view DOM content"):
        st.text_area("DOM content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe whant you want to parse ?")

    if st.button("Parse content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result= parse_with_ollama(dom_chunks, parse_description)
            st.write(result)