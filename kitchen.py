import re
import nltk
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')

def clean_text(text):
    text = re.sub(r'<.*?>', '', text) #Remove HTML tags
    text = re.sub(r'[^a-zA-Z]', ' ', text) #Remove punctuation
    text = text.lower() #Convert to lowercase
    text = text.split() #Split the text
    text = [word for word in text if not word in set(stopwords)] #Remove stopwords
    text = ' '.join(text)
    return text

def stemmer(text):
    text = text.split()
    stemmer = nltk.PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text]
    text = ' '.join(stemmed_words)
    return text