import streamlit as st
import requests

st.title("Yield Predictor 🌾")

# All the sliders you need based on your API call
N = st.slider("Nitrogen (N)", 0, 500)
P = st.slider("Phosphorous (P)", 0, 50)
K = st.slider("Potassium (K)", 0, 800)
pH = st.slider("pH Level", 4.5, 9.0)
EC = st.slider("Electrical Conductivity (EC)", 0.0, 5.0)
OC = st.slider("Organic Carbon (OC)", 0.0, 5.0)
S = st.slider("Sulfur (S)", 0, 100)
Zn = st.slider("Zinc (Zn)", 0.0, 10.0)
Fe = st.slider("Iron (Fe)", 0.0, 50.0)
Cu = st.slider("Copper (Cu)", 0.0, 10.0)
Mn = st.slider("Manganese (Mn)", 0.0, 50.0)
B = st.slider("Boron (B)", 0.0, 5.0)

if st.button("Predict"):
    try:
        # Fixed the API call with proper syntax
        response = requests.get(
            "http://api:8000/predict", 
            params={
                "N": N, 
                "P": P, 
                "K": K, 
                "pH": pH,
                "EC": EC,
                "OC": OC,
                "S": S,
                "Zn": Zn,
                "Fe": Fe,
                "Cu": Cu,
                "Mn": Mn,
                "B": B
            }
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Yield Class: {result['predicted_class']}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Make sure your prediction service is running.")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {str(e)}")
    except KeyError:
        st.error("Unexpected response format from API")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")