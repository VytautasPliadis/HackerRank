<<<<<<< HEAD
import random

print(random.uniform(2,3))
=======
import plotly.express as px
import streamlit as st

# Sample data
x = [1, 2, 3, 4, 5]  # X-axis values
y1 = [10, 12, 8, 14, 9]  # Y-axis values for the first line
y2 = [5, 7, 6, 8, 7]  # Y-axis values for the second line

# Create a line chart with custom line names
fig = px.line(x=x, y=[y1, y2], labels={'x': 'X-axis Label', 'y': 'Y-axis Label'},
              title='Line Chart with Custom Line Names')

# Set custom line names for the legend
fig.update_layout(legend_title='Custom Line Names')
fig.data[0].name = 'Custom Line Name 1'
fig.data[1].name = 'Custom Line Name 2'

st.write(fig)
>>>>>>> 299bb212a146bad85f7260176531b4b8f2cc923e
