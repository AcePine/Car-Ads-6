import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')


# creating first scatter plot using plotly-express
st.header('Price of Cars by Manufacturer')

fig_scatter = px.scatter(df, x='type', y='price')

st.plotly_chart(fig_scatter)


st.header('Average Car Listed for 24 Days')

fig_bar = px.bar(df, x='days_listed', y='model_year')

st.plotly_chart(fig_bar)


st.header('Most Popular Car For Sale is from 2011')

fig_histo = px.histogram(df, x='model_year')

# fig_histo.show()

st.plotly_chart(fig_histo)


st.header('Most Listed Cars Have Between 120k-125k Miles')

# Create a checkbox
show_outliers = st.checkbox('Show Outliers')

# Filter the data based on the checkbox value
if show_outliers:
    filtered_df = df
else:
    filtered_df = df[df['odometer'].between(0, 300000)]

# Create the histogram using the filtered data
fig_histo_2 = px.histogram(filtered_df, x='odometer')

# Display the histogram
st.plotly_chart(fig_histo_2)
