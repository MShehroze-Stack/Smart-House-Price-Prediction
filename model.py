import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Data load karna
data = pd.read_csv('house_data.csv')
print("Dataset loaded successfully!")
print(data)

# 2. Inputs aur Output alag karna
X = data[['Area_SqFt', 'Rooms']]
y = data['Price_PKR']

# 3. Model banana aur train karna
model = LinearRegression()
model.fit(X, y)
print("\nAI Model successfully train ho gaya hai!")

# 4. Test prediction (Simple tareeqa)
predicted_price = model.predict([[1600, 3]])
price_answer = int(predicted_price[0])
print("\nPrediction Result:")
print("1600 SqFt aur 3 rooms wale ghar ki qeemat hogi: PKR", price_answer)