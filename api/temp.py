import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import Ridge


# Cargar una parte del dataset
num_rows = 10000  # Especifica el número de filas que deseas leer
df = pd.read_csv('Clean_Dataset.csv', nrows=num_rows)

# Limpiar y preparar datos
# Aquí puedes incluir la eliminación de valores nulos, conversión de tipos de datos, etc.

# Análisis básico como df.describe(), df.info(), etc.

# Seleccionar columnas categóricas y numéricas
cat_columns = ['airline', 'flight', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class']
num_columns = ['duration', 'days_left']

# Crear transformadores para columnas categóricas y numéricas
cat_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
num_transformer = Pipeline(steps=[('scaler', StandardScaler())])

# ColumnTransformer para aplicar transformaciones
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, num_columns),
        ('cat', cat_transformer, cat_columns)])

# Definir X e y
X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear pipeline con preprocesador y modelo
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', RandomForestRegressor())])

# Entrenar modelo
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar modelo
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Coefficient of Determination (R^2):", r2_score(y_test, y_pred))

# Aquí puedes incluir ajustes en los hiperparámetros, probar diferentes modelos, etc.
