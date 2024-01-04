import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 设置页面标题
st.title("Word Cloud Generator")

# 接收用户输入的文本
text = st.text_area("Enter text:")

# 当用户点击按钮时生成词云图
if st.button("Generate Word Cloud"):
    # 创建词云对象并生成词云图
    wordcloud = WordCloud().generate(text)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()

