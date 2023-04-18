import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')


# creating a scatter plot for price distribution

st.header('Distribution of Prices by Odemeter Count')

fig_scatter_new = px.scatter(df, x='price', y='odometer', color='condition', hover_data=['model', 'manufacturer'],
                             color_discrete_map={
                                "new": "green",
                                "like new": "blue",
                                "excellent": "orange",
                                "good": "yellow",
                                "fair": "red",
                                "salvage": "black"
                             },
                             category_orders={'condition': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']})

fig_scatter_new.update_layout(xaxis_title='Price', yaxis_title='Odometer')

show_outliers_scatter = st.checkbox('Show Outliers', value=False)

if show_outliers_scatter:
    fig_scatter_new.update_layout(xaxis_range=[0, 350000])
    fig_scatter_new.update_layout(yaxis_range=[0,500000])
else:
    fig_scatter_new.update_layout(xaxis_range=[0, 100000])
    fig_scatter_new.update_layout(yaxis_range=[0,350000])

fig_scatter_new.show()

# st.plotly_chart(fig_scatter_new)


# creating a histogram for price distribution

st.header('Distribution of Prices by Condition')

fig_histo_new = px.histogram(df, x='price', color='condition', marginal='rug',
                             color_discrete_map={
                                "new": "green",
                                "like new": "blue",
                                "excellent": "orange",
                                "good": "yellow",
                                "fair": "red",
                                "salvage": "black"
                             },
                             category_orders={'condition': ['new', 'like new', 'excellent', 'good', 'fair', 'salvage']}
                             )

fig_histo_new.update_layout(xaxis_title='Price', yaxis_title='Count')

show_rug = st.checkbox('Show Rug Plot')

show_outliers = st.checkbox('Show Outliers', value=False)

if show_outliers:
    fig_histo_new.update_layout(xaxis_range=[0, 350000])
else:
    fig_histo_new.update_layout(xaxis_range=[0, 100000])

fig_histo_new.show()

st.plotly_chart(fig_histo_new)
