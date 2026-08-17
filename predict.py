import joblib
from sklearn.datasets import load_breast_cancer

# Load dataset
data = load_breast_cancer()

# Load trained model
model = joblib.load("models/best_model.pkl")

# Select one sample
sample = data.data[0].reshape(1, -1)

# Prediction
prediction = model.predict(sample)

print("Predicted class:", data.target_names[prediction[0]])
print("Actual class:", data.target_names[data.target[0]])
