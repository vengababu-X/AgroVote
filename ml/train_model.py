import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("dataset.csv")

X = data.drop("crop", axis=1)
y = data["crop"]

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Models
dt = DecisionTreeClassifier()
nb = GaussianNB()
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Voting Ensemble
model = VotingClassifier(
    estimators=[
        ('dt', dt),
        ('nb', nb),
        ('rf', rf)
    ],
    voting='hard'
)

# Train
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((model, encoder), f)

print("Model trained and saved")
