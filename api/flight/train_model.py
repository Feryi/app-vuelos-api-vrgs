import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Data Preparation
df = pd.read_csv('./../Clean_Dataset.csv', nrows=10000)  # Lee solo las primeras 10,000 filas
df.dropna(inplace=True)  # Remove missing values

# Step 2: Feature Engineering
# Convert categorical columns to numeric
label_encoders = {}
for column in ['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Separate features and target variable
X = df.drop('price', axis=1)
y = df['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Selection
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Step 4: Training the Model
model.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 6: Saving the Model
joblib.dump(model, 'flight_price_predictor.pkl')
