# Flight Ticket Price Prediction using SGD Model

This project leverages machine learning techniques to predict flight ticket prices based on various features such as departure and arrival times, airlines, origin and destination cities, and other relevant factors. The model used for the prediction is the Stochastic Gradient Descent (SGD) algorithm.

## Project Overview

Flight ticket prices can vary significantly depending on numerous factors, such as time of booking, flight duration, airline, and more. In this project, we aim to predict flight ticket prices using an SGD model, which is an optimization method for linear regression. The dataset used for training and testing contains historical flight data, including both structured and categorical features.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data](#data)
- [Model](#model)
- [Training](#training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [License](#license)

## Getting Started

To get started with this project, you can clone the repository and install the necessary dependencies. Follow the instructions below to set up the environment and run the project on your local machine.

### Cloning the Repository

```bash
git clone https://github.com/yourusername/flight-ticket-price-prediction.git
cd flight-ticket-price-prediction
```

## Prerequisites
Before running the project, ensure you have the following tools and libraries installed:

Python 3.x
pip (Python package manager)

## Installation 

Follow the steps below to set up the environment and install the necessary dependencies for this project.

## Step 1: Clone the Repository

First, clone the repository to your local machine by running the following command:

```bash
git clone https://github.com/yourusername/flight-ticket-price-prediction.git
```
Replace yourusername with your GitHub username or the appropriate username of the repository.

## Step 2: Navigate to the Project Directory

After cloning the repository, navigate into the project directory:

```bash
cd flight-ticket-price-prediction
```
## Step 3: Install the Required Dependencies

## Data
The dataset used in this project contains historical flight data including features such as:

- Airline: The airline operating the flight.
- Origin: The origin airport.
- Destination: The destination airport.
- Departure Time: The scheduled departure time of the flight.
- Arrival Time: The scheduled arrival time.
- Duration: The duration of the flight.
- Price: The flight ticket price (target variable).
  
You can find the dataset in the data folder or you may need to download it from a public source 

## Model

This project uses Stochastic Gradient Descent (SGD) as the optimization method for linear regression. The model is trained to predict the price of a flight ticket based on the features provided in the dataset.

Model Summary:
- Model: Stochastic Gradient Descent Regressor
- Loss function: Mean Squared Error (MSE)
- Evaluation metric: Mean Absolute Error (MAE)

## Training

Once the dependencies are installed and the data is ready, you can train the model by running the train.py script.

```bash
python train.py
```

This will:

Load and preprocess the dataset.
Train the SGD model using the training data.
Save the trained model as a .pkl file.
