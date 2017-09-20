import nltk
from nltk.corpus import stopwords
import codecs
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

TEXT_FILE = 'resources/LaVanguardia.txt'

def readFile():
	# Read the file TEXT_FILE and return the list of lines.
	print("Loading file",TEXT_FILE)
	f = codecs.open(TEXT_FILE,'r','latin1')
	content = f.readlines()
	return content

def tokenize(text):
	# Tokenize and normalize the given text.
	tokens = nltk.word_tokenize(text)

	tokens = [token.lower() for token in tokens]	# All tokens to lowercase

	words = [token for token in tokens if token.isalpha()]	# Maintain strings with alphabetic characters

	wnl = nltk.WordNetLemmatizer()
	lemmatized = [wnl.lemmatize(t) for t in words] # Lemmatization

	return lemmatized


def vectorize(texts):
	# Vectorization using the CountVectorizer.
	print("\nVectorization started")
	vectorizer = CountVectorizer(input='content',tokenizer=tokenize,stop_words=stopwords.words('spanish'))
	matrix = vectorizer.fit_transform(texts)
	print("Total features:",len(vectorizer.get_feature_names()))
	print("Matrix shape",str(matrix.shape))
	print("Vectorization finished")
	return matrix


def gen_clusters(vectors):
	# Generate words clusters using the k-means algorithm.
	print("\nClustering started")
	km_model = KMeans(n_clusters=8)
	km_model.fit(vectors)
	print("Labels: ",km_model.labels_)
	print("Clustering finished")


if __name__ == "__main__":

	file_content = readFile() # Read the TEXT_FILE

	vectors = vectorize(file_content) # Vectorize

	gen_clusters(vectors) # Generate clusters

