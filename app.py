import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

model=pickle.load(open('LinearRegressionModel.pkl','rb'))
df_imported=pd.read_csv('df_cleaned.csv')
df=df_imported.iloc[:,1:]
st.title('Used car price prediction')
st.sidebar.header("Enter Car Details")
company = st.sidebar.selectbox("Company",(sorted(set(df['company']))))
year_of_purchase = st.sidebar.selectbox("Year of Purchase",(sorted (set(df['year']),reverse=True)))
fuel_type = st.sidebar.selectbox("Fuel Type", (sorted (set(df['fuel_type']))))
kms_driven = st.sidebar.number_input("Kilometers Driven", 0, 500000, 50000)

filtered_models = df[df['company'] == company]['name'].unique()
car_model = st.selectbox("Enter your car with model name", sorted(filtered_models))
def predict(company, car_model, year_of_purchase, fuel_type, kms_driven):
    company=company
    car_model=car_model
    year=year_of_purchase
    fuel_type=fuel_type
    driven=kms_driven
    my_dict = {"name":car_model, "company":company, "year":year, "kms_driven":driven, "fuel_type":fuel_type }
    df_1= pd.DataFrame.from_dict([my_dict])
    predicted_price=model.predict(df_1)
    print(predicted_price)
    return predicted_price[0]

if st.button("Predict the Price"):
    if not car_model:  # Check if the car model input is empty
        st.error("Please enter the car model!")
    else:
        price = predict(company, car_model, year_of_purchase, fuel_type, kms_driven)
        st.success(f"The predicted price of the car is: ₹{price:,.2f}")
    