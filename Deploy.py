import streamlit as st
import pandas as pd
import joblib
from datetime import date, datetime, timedelta

# Load the saved pipeline
pipeline = joblib.load("best_model.pkl")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About the Project", "Prediction"])

if page == "About the Project":
    # About the Project Page
    st.title("About the Project")
    st.write("""
    This Flight Price Prediction app is designed to help users estimate the cost of flights based on 
    various factors such as airline, source, destination, and additional information.

    ### Features
    - Predict flight ticket prices using a machine learning model.
    - Input customizable flight details like duration, stops, departure and arrival times.

    ### Technology Used
    - **Streamlit** for building the interactive web app.
    - **Scikit-learn** for the machine learning pipeline.
    - **Joblib** for model serialization.

    ### Author
    Developed by [Your Name].
    """)

elif page == "Prediction":
    # Prediction Page
    st.title("Flight Price Prediction App")

    st.sidebar.header("Input Features")

    def user_input_features():
        Airline = st.sidebar.selectbox("Airline", ["Air India", "IndiGo", "Jet Airways", "SpiceJet", "Vistara",
                                                   "Multiple carriers", "Air Asia", "GoAir", 
                                                   "Multiple carriers Premium economy", 
                                                   "Vistara Premium economy", "Trujet"])
        Source = st.sidebar.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Banglore"])
        Destination = st.sidebar.selectbox("Destination", ["Banglore", "Delhi", "Kolkata", "Mumbai", "Chennai",
                                                            "Cochin", "New Delhi", "Hyderabad"])
        
        # Duration as time input
        Duration_Time = st.sidebar.time_input("Duration (HH:MM)")
        Duration = Duration_Time.hour * 60 + Duration_Time.minute  # Convert to minutes
        
        Total_Stops = st.sidebar.number_input("Total Stops", min_value=0.0, max_value=5.0, step=1.0)
        Additional_Info = st.sidebar.selectbox("Additional Info", ["No info", "In-flight meal not included",
                                                                   "No check-in baggage included", "1 Long layover",
                                                                   "Change airports", "Red-eye flight"])
        
        # Departure Date and Time
        Dep_Date = st.sidebar.date_input("Departure Date",value = date(2019, 1, 1))
        Dep_Time = st.sidebar.time_input("Departure Time")
        
        # Calculate Arrival Date and Month
        Dep_DateTime = datetime.combine(Dep_Date, Dep_Time)
        Arrival_DateTime = Dep_DateTime + timedelta(minutes=Duration)
        Arrival_Day = Arrival_DateTime.day
        Arrival_Month = Arrival_DateTime.month
        
        # Store user input in a dataframe
        data = {
            "Airline": [Airline],
            "Source": [Source],
            "Destination": [Destination],
            "Duration": [Duration],
            "Total_Stops": [Total_Stops],
            "Additional_Info": [Additional_Info],
            "Dep_Hour": [Dep_Time.hour],
            "Dep_Minute": [Dep_Time.minute],
            "Journey_Day": [Dep_Date.day],
            "Journey_Month": [Dep_Date.month],
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
