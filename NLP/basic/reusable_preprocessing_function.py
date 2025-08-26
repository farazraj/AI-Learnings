import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download NLTK resources (only first time)
nltk.download("punkt")
nltk.download("stopwords")

# Load spaCy model (only once)
nlp = spacy.load("en_core_web_sm")

# Initialize stemmer
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text, use_stemming=True, use_lemmatization=False):
    """
    Preprocess a given text string.
    
    Steps:
    1. Tokenization
    2. Stopword Removal
    3. Stemming or Lemmatization
    
    Args:
        text (str): The input sentence/document.
        use_stemming (bool): Apply stemming if True.
        use_lemmatization (bool): Apply lemmatization if True.
    
    Returns:
        List of processed tokens.
    """
    
    # Tokenization
    tokens = word_tokenize(text.lower())
    
    # Stopword Removal
    filtered_tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    
    # Apply Stemming
    if use_stemming and not use_lemmatization:
        processed = [stemmer.stem(w) for w in filtered_tokens]
    
    # Apply Lemmatization
    elif use_lemmatization and not use_stemming:
        doc = nlp(" ".join(filtered_tokens))
        processed = [token.lemma_ for token in doc]
    
    # If neither selected, just return tokens
    else:
        processed = filtered_tokens
    
    return processed


print(preprocess_text("Hi There, don't try to act smart", False, True))