import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# =========================
# Load dataset
# =========================
df = pickle.load(open("laptop_cleaned.pkl", "rb"))

# =========================
# Separate X & y
# =========================
X = df.drop("price", axis=1)
y = df["price"]

# =========================
# Train-test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Train model
# =========================
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# Check accuracy
# =========================
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# =========================
# Save model + columns
# =========================
pickle.dump(
    {
        "model": model,
        "columns": X_train.columns.tolist()
    },
    open("laptop_price_model.pkl", "wb")
)

print("✅ Model saved successfully")
