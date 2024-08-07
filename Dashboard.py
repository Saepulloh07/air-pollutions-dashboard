import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
data = pd.read_csv('Dashboard/all_data.csv')

# Sidebar for user inputs
st.sidebar.header('User Input Features')
year = st.sidebar.selectbox('Year', sorted(data['year'].unique()))
station = st.sidebar.selectbox('Station', sorted(data['station'].unique()))

# Filter data based on user input
filtered_data = data[(data['year'] == year) & (data['station'] == station)]

st.header('Air Pollution Quality Dashboard')
# Pertanyaan 1: Variasi konsentrasi O3 harian berkaitan dengan perubahan suhu harian dan radiasi matahari
st.header('Perubahan suhu dan konsentrasi O3')
daily_data = filtered_data.groupby('day').agg({'O3': 'mean', 'TEMP': 'mean'}).reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=daily_data, x='day', y='O3', ax=ax1, label='O3')
ax2 = ax1.twinx()
sns.lineplot(data=daily_data, x='day', y='TEMP', ax=ax2, color='r', label='Temperature')
ax1.set_xlabel('Day')
ax1.set_ylabel('O3 Concentration')
ax2.set_ylabel('Temperature')
st.pyplot(fig1)

# Pertanyaan 2: Pola musiman dalam tingkat polusi PM10 dan hubungan dengan curah hujan bulanan
st.header('tingkat polusi PM10 dan hubungan dengan curah hujan')
monthly_data = filtered_data.groupby('month').agg({'PM10': 'mean', 'RAIN': 'sum'}).reset_index()
fig2, ax3 = plt.subplots()
sns.barplot(data=monthly_data, x='month', y='PM10', ax=ax3, label='PM10')
ax4 = ax3.twinx()
sns.lineplot(data=monthly_data, x='month', y='RAIN', ax=ax4, color='g', label='Rain')
ax3.set_xlabel('Month')
ax3.set_ylabel('PM10 Concentration')
ax4.set_ylabel('Rainfall')
st.pyplot(fig2)

# Additional visualization 1: Distribution of pollutants
st.header('Distribution of Pollutants')
fig3, ax5 = plt.subplots()
sns.histplot(filtered_data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']], kde=True, ax=ax5)
ax5.set_xlabel('Concentration')
ax5.set_ylabel('Frequency')
st.pyplot(fig3)

# Additional visualization 2: Wind direction and speed
st.header('Wind Direction and Speed')
fig4, ax6 = plt.subplots()
sns.scatterplot(data=filtered_data, x='WSPM', y='TEMP', hue='wd', ax=ax6)
ax6.set_xlabel('Wind Speed (WSPM)')
ax6.set_ylabel('Temperature')
st.pyplot(fig4)

# Additional visualization 3: Time series plot of pollutants
st.header('Time Series Plot of Pollutants')
fig5, ax7 = plt.subplots()
sns.lineplot(data=filtered_data, x='hour', y='PM2.5', ax=ax7, label='PM2.5')
sns.lineplot(data=filtered_data, x='hour', y='PM10', ax=ax7, label='PM10')
sns.lineplot(data=filtered_data, x='hour', y='SO2', ax=ax7, label='SO2')
sns.lineplot(data=filtered_data, x='hour', y='NO2', ax=ax7, label='NO2')
sns.lineplot(data=filtered_data, x='hour', y='CO', ax=ax7, label='CO')
sns.lineplot(data=filtered_data, x='hour', y='O3', ax=ax7, label='O3')
ax7.set_xlabel('Hour')
ax7.set_ylabel('Concentration')
st.pyplot(fig5)
