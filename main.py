import streamlit as st
import plotly.express as px

st.title("Weather Forecast  for the Next Days")
place = st.text_input("Place:  ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Add graph chart,import and use plotly.express library
# Create a figure , use x, y and name

def gat_dates(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = gat_dates(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)