import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


#streamlit app
st.title("💳 Online Payment Fraud Detection")
st.write("Enter transaction details to check if its fraudulent or not.")

#user inputs
# step = st.number_input("Transaction Step(Hour)" , min_value = 0 , format = "%d")
transaction_type = st.selectbox("Transaction type " , ["CASH-IN" , "CASH-OUT" , "DEBIT", "PAYMENT", "TRANSFER"])
amount = st.number_input("Transaction Amount " , min_value = 0.0 , format = "%.2f")
old_balance = st.number_input("Old Balance (before Transaction)" , min_value=0.0, format = "%.2f" )
new_balance = st.number_input("New Balance (After Transaction) ",min_value = 0.0 , format = "%.2f")

# encoding transaction type
transaction_mapping = {"CASH-IN":0 , "CASH-OUT":1 , "DEBIT":2, "PAYMENT":3, "TRANSFER":4}
transaction_encoded = transaction_mapping[transaction_type]

#create input array
features = np.array([[transaction_encoded , amount , old_balance , new_balance]])

# prediction button
if st.button("Check Transaction"):
    predictions = model.predict(features)[0]

    if predictions == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Safe.")