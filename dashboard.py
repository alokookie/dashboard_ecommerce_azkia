import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Analisis E-Commerce")

# load data dari csv
top_3 = pd.read_csv('top_3.csv')
bottom_3 = pd.read_csv('bottom_3.csv')
avg_items = pd.read_csv('avg_items.csv')['avg_items'][0]
avg_monthly = pd.read_csv('avg_monthly.csv')

# Kategori produk yang sering dan paling jarang dibeli customer
st.subheader("Kategori Produk")

col1, col2 = st.columns(2)

with col1:
    st.write("Top 3 Kategori Paling Sering Dibeli")
    st.dataframe(top_3)

with col2:
    st.write("Top 3 Kategori Paling Jarang Dibeli")
    st.dataframe(bottom_3)

# Rata-rata jumlah produk dalam satu pesanan

st.subheader("Rata-rata Produk per Order")
st.metric("Rata-rata", f"{avg_items:.2f}")

# Tren Transaksi Bulana

st.subheader("Tren Transaksi Bulanan")

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(data=avg_monthly, x='month', y='price', ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)