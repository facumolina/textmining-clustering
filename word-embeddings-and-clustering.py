import nltk
from nltk.corpus import stopwords
import codecs
import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
import string
from gensim.models import Word2Vec

TEXT_FILE = 'resources/LaVanguardia.txt'

def readFile():
	# Read the file TEXT_FILE and return the list of lines.
	print("Loading file",TEXT_FILE)
	f = codecs.open(TEXT_FILE,'r','latin1')
	content = f.read()
	return content

def tokenize(text):
	# Tokenize and normalize the given text.
	sents = nltk.sent_tokenize(text)
	
	sents = [sent.lower() for sent in sents]	# All sentences to lowercase

	#exclude = set(string.punctuation)
	#sents = [''.join(ch for ch in sent if ch not in exclude) for sent in sents]	# Remove punctuation from sentences

	sents = [re.sub(r'\d+', '', sent) for sent in sents] # Remove numbers

	sents = [re.sub(r'([^\s\w]|_)+', '', sent) for sent in sents] # Only alphabetic characters

	#wnl = nltk.WordNetLemmatizer()
	#lemmatized = [wnl.lemmatize(t) for t in sents] # Lemmatization
	tokenized_sents = [nltk.word_tokenize(sent) for sent in sents]

	return tokenized_sents


def gen_clusters(vectors):
	# Generate words clusters using the k-means algorithm
	print("\nClustering started")
	km_model = KMeans(n_clusters=8)
	km_model.fit(vectors)
	print("Labels: ",km_model.labels_)
	print("Clustering finished")


if __name__ == "__main__":

	file_content = readFile() # Read the TEXT_FILE

	normalized = tokenize(file_content)

	#gen_clusters(vectors) # Generate clusters
	model = Word2Vec(normalized,min_count=1)
	model.save('the_model')
	model = Word2Vec.load('the_model')


