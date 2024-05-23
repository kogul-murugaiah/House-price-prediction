import streamlit as st
import pandas as pd
import pickle

# Load the data and model
data = pd.read_csv('final_dataset.csv')
model = pickle.load(open("RidgeModel.pkl", 'rb'))

# Define function to predict price
def predict_price(beds, baths, size, zip_code):
    # Convert inputs to appropriate data types
    try:
        beds = int(beds)
        baths = float(baths)
        size = float(size)
        zip_code = int(zip_code)
    except ValueError:
        st.error("Invalid input values. Please enter valid numeric values.")
        return None

    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[beds, baths, size, zip_code]],
                              columns=['beds', 'baths', 'size', 'zip_code'])

    # Predict the price
    prediction = model.predict(input_data)[0]
    return prediction

# Streamlit app
def main():
    st.title('House Price Prediction')

    st.write('Welcome to House Price Prediction Model!')

    # Input fields
    beds_placeholder = 'Select number of bedrooms'
    baths_placeholder = 'Select number of bathrooms'
    size_placeholder = 'Select size of the house'
    zip_code_placeholder = 'Select zip code'

    beds = st.selectbox('Bedrooms', [beds_placeholder] + list(data['beds'].unique()))
    baths = st.selectbox('Baths', [baths_placeholder] + list(data['baths'].unique()))
    size = st.selectbox('Size', [size_placeholder] + list(data['size'].unique()))
    zip_code = st.selectbox('Zip Code', [zip_code_placeholder] + list(data['zip_code'].unique()))

    if st.button('Predict Price'):
        if beds == beds_placeholder or baths == baths_placeholder or size == size_placeholder or zip_code == zip_code_placeholder:
            st.error('Please select values for all input fields.')
        else:
            prediction = predict_price(beds, baths, size, zip_code)
            if prediction is not None:
                st.success(f'Predicted Price: INR {prediction}')

if __name__ == "__main__":
    main()
