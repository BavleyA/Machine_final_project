import streamlit as st
import pandas as pd
import joblib

# Load the saved pipeline
pipeline = joblib.load("best_model.pkl")

# Streamlit app title
st.title("Flight Price Prediction App")

# Input form
st.sidebar.header("Input Features")

def user_input_features():
    Airline = st.sidebar.selectbox("Airline", ["Air India", "IndiGo", "Jet Airways", "SpiceJet", "Vistara" ,"Multiple carriers" ,"Air Asia " , "GoAir ", "Multiple carriers Premium economy", "Vistara Premium economy","Trujet "])
    Source = st.sidebar.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Banglore"])
    Destination = st.sidebar.selectbox("Destination", ["Banglore", "Delhi", "Kolkata", "Mumbai", "Chennai" ,"Cochin" ,"New Delhi" ,"Hyderabad"])
    Duration = st.sidebar.number_input("Duration (minutes)", min_value=5, max_value=2000 ,value=5)
    Total_Stops = st.sidebar.number_input("Total Stops", min_value = 0.0, max_value = 5.0 , step=1.0)
    Additional_Info = st.sidebar.selectbox("Additional Info", ["No info", "In-flight meal not included", "No check-in baggage included" ,"1 Long layover " ,"Change airports","Red-eye flight"])
    Dep_Hour = st.sidebar.number_input("Departure Hour", min_value=0, max_value=23, value=12)
    Dep_Minute = st.sidebar.number_input("Departure Minute", min_value=0, max_value=59, value=30)
    Journey_Day = st.sidebar.number_input("Journey Day", min_value=1, max_value=31, value=15)
    Journey_Month = st.sidebar.number_input("Journey Month", min_value=1, max_value=12, value=6)
    Arrival_Day = st.sidebar.number_input("Arrival Day", min_value=1, max_value=31, value=15)
    Arrival_Month = st.sidebar.number_input("Arrival Month", min_value=1, max_value=12, value=6)

    # Store user input in a dataframe
    data = {
        "Airline": [Airline],
        "Source": [Source],
        "Destination": [Destination],
        "Duration": [Duration],
        "Total_Stops": [Total_Stops],
        "Additional_Info": [Additional_Info],
        "Dep_Hour": [Dep_Hour],
        "Dep_Minute": [Dep_Minute],
        "Journey_Day": [Journey_Day],
        "Journey_Month": [Journey_Month],
        "Arrival_Day": [Arrival_Day],
        "Arrival_Month": [Arrival_Month]
    }
    return pd.DataFrame(data)

# Get input features
input_df = user_input_features()

# Show input dataframe
st.write("Input Data")
st.dataframe(input_df)

# Make predictions
if st.button("Predict"):
    prediction = pipeline.predict(input_df)
    st.success(f"Predicted Price: ₹{prediction[0]:.2f}")
