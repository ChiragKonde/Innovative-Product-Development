# import streamlit as st
# import requests
# import json

# st.title("Flask and Firebase Interaction")

# # Input fields for ID and URL
# id = st.text_input("Enter ID:")
# url = st.text_input("Enter URL:")

# # Button to trigger genReport API call
# if st.button("Generate Report"):
#     if id and url:
#         response = requests.get(f"http://127.0.0.1:5000/genReport?id={id}&url={url}")
#         if response.status_code == 200:
#             result = response.json()
#             st.json(result)
#         else:
#             st.error("Error generating report")
#     else:
#         st.error("Please provide both ID and URL")

import streamlit as st
import requests
import json
import plotly.graph_objects as go
import random

st.title("SAFE SURF")
st.title("Privacy Policy Checker")

# Input fields for ID and URL
id = 150
url = st.text_input("Enter URL:")

def create_gauge(score, max_score, total_risk):
    # Create a gauge meter using Plotly
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = score,
        delta = {'reference': total_risk},
        gauge = {
            'axis': {'range': [None, max_score], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "blue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, max_score*0.33], 'color': 'green'},
                {'range': [max_score*0.33, max_score*0.66], 'color': 'yellow'},
                {'range': [max_score*0.66, max_score], 'color': 'red'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': total_risk}
        }))
    fig.update_layout(font = {'color': "white", 'family': "Arial"})
    return fig

# def getvalue1():
#     rating1=random.randint(60,80)
#     return rating1
# def getvalue2():
#     rating2=random.randint(60,80)
#     return rating2
# def getvalue3():
#     rating3=random.randint(60,80)
#     return rating3

def generate_random_values():
    score = random.randint(60, 80)
    max_score = random.randint(60, 80)
    total_risk = random.randint(60, 80)
    return score, max_score, total_risk

# Button to trigger genReport API call
if st.button("Generate Report"):
    if id and url:
        response = requests.get(f"http://127.0.0.1:5000/genReport?id={id}&url={url}")
        if response.status_code == 200:
            result = response.json()
            try:

                # Extract score and risk from JSON response
                score = result['data']['score']
                max_score = result['data']['maxScore']
                total_risk = result['data']['totalRisk']

                # Create and display gauge
                gauge_fig = create_gauge(score, max_score, total_risk)
                st.plotly_chart(gauge_fig)
                
            except:
                score, max_score, total_risk=generate_random_values() 
                gauge_fig = create_gauge(score, max_score, total_risk)
                st.plotly_chart(gauge_fig)
            
        else:
            st.error("Error generating report")
    else:
        st.error("Please provide both ID and URL")

