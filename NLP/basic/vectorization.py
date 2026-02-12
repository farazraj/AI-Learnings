from reusable_preprocessing_function import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from gensim.models import Word2Vec
import numpy as np


#text to preprocess and vectorize
document = [
    "I love NLP and machine learning.",
    "NLP is amazing for text processing.",
    "Deep learning greatly advances NLP."
]


#Preprocessing of the text
prep_text = preprocess_text(''.join(document), use_stemming=False, use_lemmatization=True)
print("prep_text:", prep_text)


#Different vectorization techniques

# Bag of Words
def bag_of_words(docs):

    cv = CountVectorizer()                    # you can add options like stop_words='english'
    X_bow = cv.fit_transform(docs)            # sparse matrix: (#docs, vocab_size)

    print("Vocab:", cv.get_feature_names_out())
    print("Shape:", X_bow.shape)
    print("Dense counts matrix:\n", X_bow.toarray())


# TF-IDF
def tfidf(docs):

    tfidf = TfidfVectorizer()                 # add options like min_df, max_df, ngram_range, stop_words
    X_tfidf = tfidf.fit_transform(docs)

    print("Vocab:", tfidf.get_feature_names_out())
    print("Shape:", X_tfidf.shape)
    print("Dense TF-IDF matrix:\n", np.round(X_tfidf.toarray(), 3))


# spacy
def spacy_embeddings(docs):

    # IMPORTANT: use a model with vectors (sm model has no real vectors)
    # Install once via: python -m spacy download en_core_web_md
    nlp = spacy.load("en_core_web_md")  # or en_core_web_lg

    doc_vectors = [nlp(text).vector for text in docs]   # averaged token vectors per doc
    doc_vectors = np.vstack(doc_vectors)                # shape: (#docs, embedding_dim)

    print("Embedding shape:", doc_vectors.shape)        # e.g., (3, 300)
    print("First doc vector (first 8 dims):", np.round(doc_vectors[0][:8], 4))
    print("Mean vector (first 8 dims):", np.round(np.mean(doc_vectors, axis=0)[:8], 4))
    print("Max vector (first 8 dims):", np.round(np.max(doc_vectors, axis=0)[:8], 4))
    print("Min vector (first 8 dims):", np.round(np.min(doc_vectors, axis=0)[:8], 4))



# Word2Vec
def word2vec_embeddings(docs):

    w2v = Word2Vec(sentences=docs, vector_size=100, window=5, min_count=1, workers=4, sg=1, epochs=200)

    def doc_avg_vector(tokens):
        vecs = [w2v.wv[w] for w in tokens if w in w2v.wv]
        return np.mean(vecs, axis=0) if vecs else np.zeros(w2v.vector_size)

    doc_vecs_w2v = np.vstack([doc_avg_vector(t) for t in docs])
    print("W2V doc vectors shape:", doc_vecs_w2v.shape)   # (3, 100)


# bag_of_words(prep_text)
# tfidf(prep_text)
# spacy_embeddings(prep_text)
word2vec_embeddings(document)  # use original docs for Word2Vec
