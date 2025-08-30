''' This is a mini project creadted to check the sentiment analysis of a review if it is positive or negetaive.
There are certain steps to follow it on the basis of certain algos and processing of the data '''




'''Step 1 -  To load the datasets from the CSV file using pandas.'''

#common imports
import pandas as pd

#Load dataset
df = pd.read_csv("IMDB_Dataset.csv")

print(df.head()) #prints first 5 rows of the dataset
print(df.info()) #prints info about the dataset
print(df['sentiment'].value_counts()) #prints value counts of each sentiment  positive - 25000, negative - 25000




'''Step 2 - To preprocess the data by lowering the text, removing HTML tags, special characters, and stop words.'''

#common imports
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#Download stopwords from nltk library and create set of stopwords and stemmer
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

#Function to preprocess the text
def preprocess(text):
    # 1. Lowercase
    text = text.lower()
    # 2. Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)
    # 3. Keep only alphabets
    text = re.sub(r"[^a-z]", " ", text)
    # 4. Tokenize + remove stopwords + stem
    words = [stemmer.stem(w) for w in text.split() if w not in stop_words]
    return " ".join(words)

df['cleaned_review'] = df['review'].apply(preprocess)
print(df[['review', 'cleaned_review']].head())




'''Step 3 - To vectorize the text data using TF-IDF vectorization.'''

#common imports
from sklearn.feature_extraction.text import TfidfVectorizer

#Vectorization using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # keep top 5000 words
X = vectorizer.fit_transform(df['cleaned_review']) #features matrix
y = df['sentiment'].map({'positive':1, 'negative':0})  # encode labels and give 1 to positive and 0 to negative

print(X.shape) #prints shape of features matrix
print(y.shape) #prints shape of labels





'''Step 4 - To split the dataset into training and testing sets.'''

#common imports
from sklearn.model_selection import train_test_split


#Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape) #prints shape of training and testing sets
print(y_train.shape, y_test.shape) #prints shape of training and testing labels




'''Step 5 - To train a machine learning model (Logistic Regression) on the training data.'''

#common imports
from sklearn.linear_model import LogisticRegression

#Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)



'''Step 6 - To evaluate the model on the test data using accuracy, precision, recall, and F1-score.'''

#common imports
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using accuracy, precision, recall, and F1-score
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Display Confusion Matrix using seaborn heatmap
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap="Blues",
            xticklabels=["Negative", "Positive"],
            yticklabels=["Negative", "Positive"])
plt.show()