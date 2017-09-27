import nltk
from nltk.corpus import stopwords
from collections import Counter
import codecs
from sklearn.cluster import KMeans
from sklearn import preprocessing 
from scipy.sparse import coo_matrix
import numpy

TEXT_FILE = 'resources/LaVanguardia.txt'	# Text to be processed
MIN_FREQUENCY = 10	# Min word frequency to be considered
CLUSTERS_NUMBER = 40 # Number of clusters of words
WINDOWS_SIZE = 2 # Windows size to determine the contexts

def read_file():
	# Read the file TEXT_FILE.
	print("Loading file",TEXT_FILE)
	f = codecs.open(TEXT_FILE,'r','latin1')
	content = f.read()
	return content

def create_cooccurrence_matrix(text,tokenizer,frequent_words):
	# Create coocurrence matrix. Only create columns for those words that are in frequent_words
	print("\nCreating co-occurrence matrix")
	set_all_words={}
	set_freq_words={}
	data=[]
	row=[]
	col=[]
	sentences = nltk.sent_tokenize(text)
	for sentence in sentences:
		tokens=tokenizer(sentence) 
		for pos,token in enumerate(tokens):
			i=set_all_words.setdefault(token,len(set_all_words))
			start=max(0,pos-WINDOWS_SIZE)
			end=min(len(tokens),pos+WINDOWS_SIZE+1)
			for pos2 in range(start,end):
				if pos2==pos or tokens[pos2] not in frequent_words:
					continue
				j=set_freq_words.setdefault(tokens[pos2],len(set_freq_words))
				data.append(1.); row.append(i); col.append(j);
	cooccurrence_matrix=coo_matrix((data,(row,col)))
	print("Vocabulary size:",len(set_all_words))
	print("Matrix shape:",cooccurrence_matrix.shape)
	print("Co-occurrence matrix finished")
	return set_all_words,cooccurrence_matrix

def tokenize(text):
	# Tokenize and normalize the given text.	
	tokens = nltk.word_tokenize(text)

	tokens = [token.lower() for token in tokens]	# All tokens to lowercase

	words = [token for token in tokens if token.isalpha()]	# Maintain strings with alphabetic characters

	words = [token for token in words if token not in stopwords.words('spanish')] # Remove stopwords

	wnl = nltk.WordNetLemmatizer()
	lemmatized = [wnl.lemmatize(t) for t in words] # Lemmatization

	return lemmatized


def gen_clusters(vectors):
	# Generate word clusters using the k-means algorithm.
	print("\nClustering started")
	vectors = preprocessing.normalize(vectors)
	km_model = KMeans(n_clusters=CLUSTERS_NUMBER)
	km_model.fit(vectors)
	print("Clustering finished")
	return km_model

def frequent_words(text):
	# Returns the words that appear at least MIN_FREQUENCY times
	print("\nGetting most frequent words")
	
	words = tokens = nltk.word_tokenize(text)
	words = [token.lower() for token in words]
	wnl = nltk.WordNetLemmatizer()
	words = [wnl.lemmatize(t) for t in words] # Lemmatization

	most_frequents = []
	counter = Counter(words)
	for w in counter:
		if (counter[w]>=MIN_FREQUENCY):
			most_frequents.append(w)
	print("Most frequent words calculated. Total:",str(len(most_frequents)))
	return most_frequents

def show_results(model):
	# Show results
	c = Counter(sorted(model.labels_))
	print("\nTotal clusters:",len(c))
	for cluster in c:
		print ("Cluster#",cluster," - Total words:",c[cluster])

if __name__ == "__main__":

	file_content = read_file() # Read the TEXT_FILE

	frequent_words = frequent_words(file_content) # Get the most frequent words

	vocabulary, vectors = create_cooccurrence_matrix(file_content,tokenize,frequent_words) # Create the co-occurrence matrix

	km_model = gen_clusters(vectors) # Generate clusters

	show_results(km_model)
