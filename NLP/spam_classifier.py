import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load local CSV
df = pd.read_csv("spam.csv", encoding="latin-1")  # encoding needed to read special characters

# Rename relevant columns
df = df.rename(columns={"v1": "label", "v2": "message"})

# Drop any extra unnamed columns if present
df = df[["label", "message"]]

# Convert labels to binary
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

# Vectorize the text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Predict
y_pred = clf.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")


# Predict function
def predict_message(msg):
    vec_msg = vectorizer.transform([msg])
    pred = clf.predict(vec_msg)[0]
    return "Spam" if pred == 1 else "Ham"

test_msg = "Congratulations! You've won a free ticket. Call now!"
print(f"Prediction for test message in spam classifier: {predict_message(test_msg)}")


import joblib

# Save model and vectorizer
joblib.dump(clf, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
