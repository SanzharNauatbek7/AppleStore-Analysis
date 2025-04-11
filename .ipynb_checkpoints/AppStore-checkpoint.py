import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("AppleStore.csv")
    df.dropna(subset=["user_rating"], inplace=True)
    df = df[df["user_rating"] > 0]
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

df = load_data()

st.title("Анализ пользовательской активности на платформе")

st.write("""
    Данный проект анализирует поведение пользователей мобильных приложений на платформе. 
    Мы исследуем рейтинги, цены, сегментацию пользователей и строим воронку.
""")

st.markdown("**Разработчик**: Науатбек Санжар — Data Analyst")
st.markdown("Вы можете найти исходный код и другие проекты на моем [GitHub](https://github.com/SanzharNauatbek7)")


st.subheader("Распределение рейтингов приложений")
fig1 = px.histogram(df, x='user_rating', nbins=20, title='Распределение рейтингов приложений')
fig1.update_layout(
    xaxis_title="Рейтинг",
    yaxis_title="Частота",
    template="plotly_dark"
)
st.plotly_chart(fig1, use_container_width=True)

genre_segment = df.groupby('prime_genre').agg({'user_rating': 'mean'}).reset_index()
fig2 = px.bar(genre_segment, x='prime_genre', y='user_rating', title='Средний рейтинг по жанрам')
fig2.update_layout(
    xaxis_title="Жанр",
    yaxis_title="Средний рейтинг",
    template="plotly_dark",
    xaxis_tickangle=45
)
st.plotly_chart(fig2, use_container_width=True)

ltv = df.groupby('prime_genre').agg({'price': 'mean'}).reset_index()
fig3 = px.bar(ltv, x='prime_genre', y='price', title='Средний LTV по жанрам')
fig3.update_layout(
    xaxis_title="Жанр",
    yaxis_title="Средний LTV (Цена)",
    template="plotly_dark",
    xaxis_tickangle=45
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Воронка пользовательской активности")
stages = ['App Downloaded', 'App Opened', 'Registered', 'Active Users']
users_count = [10000, 8000, 6000, 5000]
fig4 = px.bar(x=stages, y=users_count, title='Воронка пользовательской активности')
fig4.update_layout(
    xaxis_title="Этап",
    yaxis_title="Количество пользователей",
    template="plotly_dark"
)
st.plotly_chart(fig4, use_container_width=True)
