import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

st.title("🏡 Smart House Price Prediction System")
st.write("Area aur Rooms ki tadad darj karein aur foran ghar ki qeemat maloom karein!")

# CSV file se data load karne ki koshish
try:
  data = pd.read_csv("house_data.csv")
  X = data[["Area_SqFt", "Rooms"]]
  y = data["Price_PKR"]

  model = LinearRegression()
  model.fit(X, y)
  model_ready = True
except Exception as e:
  st.error(
      f"Masla yeh hai: {e}. Baraye meharbani check karein ke 'house_data.csv'"
      " maujood hai."
  )
  model_ready = False

# User Inputs aur Prediction
if model_ready:
  area = st.number_input(
      "Ghar ka Area (Square Feet mein):", min_value=100, value=1500, step=50
  )
  rooms = st.number_input("Rooms ki Tadad:", min_value=1, value=3, step=1)

  if st.button("Predict Price"):
    prediction = model.predict([[area, rooms]])
    price = int(prediction[0])
    st.success(f"Estimated House Price: PKR {price:,}")