import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

# 1. Page Title
st.title("🏡 Smart House Price Prediction System")
st.write("Area aur Rooms ki tadad darj karein aur foran ghar ki qeemat maloom karein!")

# 2. Inline Model Training (Data direct read hoga)
try:
  data = pd.read_csv("house_data.csv")
  X = data[["Area_SqFt", "Rooms"]]
  y = data["Price_PKR"]

  model = LinearRegression()
  model.fit(X, y)
  model_ready = True
except Exception as e:
  st.error(f"Dataset load karne mein masla hai: {e}")
  model_ready = False

# 3. User Inputs
if model_ready:
  area = st.number_input(
      "Ghar ka Area (Square Feet mein):", min_value=100, value=1500, step=50
  )
  rooms = st.number_input("Rooms ki Tadad:", min_value=1, value=3, step=1)

  # 4. Prediction Button
  if st.button("Predict Price"):
    prediction = model.predict([[area, rooms]])
    price = int(prediction[0])
    st.success(f"Estimated House Price: PKR {price:,}")