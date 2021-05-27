import streamlit as st
import nltk
from textblob import TextBlob
from newspaper import Article
import pandas as pd

nltk.download('punkt')

st.title('News summarizer')
url = st.text_input('News link')

article = Article(url)
article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

st.subheader('Title')
st.write(f'{article.title}')

st.write(f'Authors: {article.authors}, Date: {article.publish_date}')

st.subheader('Summary')
st.write(f'{article.summary}')

st.subheader('Sentiment')
st.write(f'Sentiment: {"positive" if analysis.polarity > 0.05 else "negative" if analysis.polarity < 0.05 else "neutral"}')

