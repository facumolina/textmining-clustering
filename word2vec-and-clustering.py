import nltk
from nltk.corpus import stopwords
from collections import Counter
import codecs
import re
from sklearn.cluster import KMeans
from sklearn import preprocessing 
from gensim.models import Word2Vec
import numpy

TEXT_FILE = 'resources/LaVanguardia.txt' # Text to be processed
CLUSTERS_NUMBER = 40 # Number of clusters of words

def readFile():
	# Read the file TEXT_FILE.
	print("Loading file",TEXT_FILE)
	f = codecs.open(TEXT_FILE,'r','latin1')
	content = f.read()
	return content

def process_tokens(tokens):
	# Process the given list of tokens
	words = [token for token in tokens if token not in stopwords.words('spanish')] # Remove stopwords

	wnl = nltk.WordNetLemmatizer()
	lemmatized = [wnl.lemmatize(t) for t in words] # Lemmatization

	return lemmatized	

def tokenize(text):
	# Tokenize and normalize the given text.
	sents = nltk.sent_tokenize(text)
	
	sents = [sent.lower() for sent in sents]	# All sentences to lowercase

	sents = [re.sub(r'\d+', '', sent) for sent in sents] # Remove numbers

	sents = [re.sub(r'([^\s\w]|_)+', '', sent) for sent in sents] # Only alphabetic characters

	tokenized_sents = [nltk.word_tokenize(sent) for sent in sents]

	tokenized_sents = [process_tokens(sent) for sent in tokenized_sents]

	return tokenized_sents

def gen_vectors(normalized_text):
	# Generate word vectors using neural word embeddings
	print("\nGenerating word vectors")
	model = Word2Vec(normalized,min_count=1)
	vects = []
	for word in model.wv.vocab:
		vects.append(model.wv[word])

	matrix = numpy.array(vects)
	print("Matrix shape:",matrix.shape)
	print("Vectors generated")
	return matrix

def gen_clusters(vectors):
	# Generate word clusters using the k-means algorithm.
	print("\nClustering started")
	vectors = preprocessing.normalize(vectors)
	km_model = KMeans(n_clusters=CLUSTERS_NUMBER)
	km_model.fit(vectors)
	print("Clustering finished")
	return km_model

def show_results(model):
	# Show results
	c = Counter(sorted(model.labels_))
	print("\nTotal clusters:",len(c))
	for cluster in c:
		print ("Cluster#",cluster," - Total words:",c[cluster])

if __name__ == "__main__":

	file_content = readFile() # Read the TEXT_FILE

	normalized = tokenize(file_content)

	vectors = gen_vectors(normalized)

	km_model = gen_clusters(vectors) # Generate clusters

	show_results(km_model)



