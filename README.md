# textmining-clustering

Práctico de Clustering para el curso [Text Mining](https://sites.google.com/view/mdt2017)

## objetivo

Encontrar grupos de palabras que puedan ser usados como clases de equivalencia, al estilo de los [Brown Clusters](https://en.wikipedia.org/wiki/Brown_clustering).

## detalles técnicos

Se utilizó el corpus _resources/LaVanguardia.txt.gz_, una recopilación de noticias del diario La Vanguardia.

Se utilizaron las siguientes herramientas:
* [nltk](http://www.nltk.org/)
* [scikit-learn](http://scikit-learn.org/stable/)
* [gensim](https://radimrehurek.com/gensim/index.html)

## proceso aplicado al corpus

### normalización
Para normalizar las palabras se dividió el texto en sentencias y para cada sentencia, se creó una lista de tokens utilizando nltk. Luego, para cada lista de sentencias
* todos los tokens fueron expresados en lowercase,
* se eliminaron los tokens que tenian caracteres no alfabéticos, 
* se eliminaron las _stopwords_ del lenguaje español (palabras muy frecuentes en el lenguaje que aportan poco valor) definidas en nltk,
* y finalmente se utilizó un proceso de lematización de cada palabra (determinar el lemma de una palabra dada).

### vectorización 

Para vectorizar las palabras se probaron dos estrategias diferentes:

1. **Vectorización con reducción de dimensionalidad mediante umbral de frecuencia**

* Se construyó la matriz de co-ocurrencia entre palabras en un contexto dado (dos palabras anteriores más las dos palabras siguientes).
* Se redujo la dimensionalidad de la matriz utilizando en las columnas sólo aquellas palabras que superaban un umbral de frecuencia dado. 
* Se obtuvieron los vectores a partir de las filas de la matriz resultante.

2. **Word embeddings neuronales**

### clustering

En ambos casos de vectorización se utilizó el algoritmo de clustering [K-means](https://en.wikipedia.org/wiki/K-means_clustering)

## resultados

1. **Clustering sobre vectores a partir de matriz de co-ocurrencias**

2. **Clustering sobre word embeddings neuronales**