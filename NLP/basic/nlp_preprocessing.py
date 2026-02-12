import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing is a powerful tool in modern AI applications."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopword Removal
filtered_tokens = [w for w in tokens if w.lower() not in stopwords.words('english')]
print("After Stopword Removal:", filtered_tokens)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in filtered_tokens]
print("After Stemming:", stemmed)

# Lemmatization (using spaCy)
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
lemmatized = [token.lemma_ for token in doc if not token.is_stop]
print("After Lemmatization:", lemmatized)
