import pandas as pd
from sklearn.linear_model import LinearRegression
import gradio as gr

# 1. Data load aur model train karna
data = pd.read_csv('house_data.csv')
X = data[['Area_SqFt', 'Rooms']]
y = data['Price_PKR']

model = LinearRegression()
model.fit(X, y)

# 2. Prediction function
def predict_price(area, rooms):
    predicted = model.predict([[area, rooms]])
    price = int(predicted[0])
    return f"Estimated House Price: PKR {price:,}"

# 3. Web Interface (UI) banana
demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Ghar ka Area (Square Feet mein)", value=1500),
        gr.Number(label="Rooms ki Tadad", value=3)
    ],
    outputs=gr.Text(label="Qeemat ka Andaza"),
    title="🏡 Smart House Price Prediction System",
    description="Area aur Rooms darj karein aur foran ghar ki qeemat maloom karein!"
)

if __name__ == "__main__":
    demo.launch(share=True)