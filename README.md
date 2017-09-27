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

**Vectorización con reducción de dimensionalidad mediante umbral de frecuencia**

* Se construyó la matriz de co-ocurrencia entre palabras en un contexto dado (dos palabras anteriores más las dos palabras siguientes).
* Se redujo la dimensionalidad de la matriz utilizando en las columnas sólo aquellas palabras que superaban un umbral de frecuencia dado. 
* Se obtuvieron los vectores a partir de las filas de la matriz resultante.

**Word embeddings neuronales**

* Se crearon los vectores de palabras a partir de una implementación de [word2vec](https://en.wikipedia.org/wiki/Word2vec), que aprende vectores para representar las palabras utilizando redes neuronales. 

### clustering

En ambos casos de vectorización se utilizó el algoritmo de clustering [K-means](https://en.wikipedia.org/wiki/K-means_clustering)

## resultados

En las ejecuciones el número de clusters elegido fue 40.

**Clustering sobre vectores a partir de matriz de co-ocurrencias**

Para este caso se utilizaron los siguientes parámetros:
* **Frecuencia mínima** = 10 (sólo se consideraron las columnas correspondientes a palabras que ocurrieran al menos 10 veces)
* **Tamaño de ventana** = 2 (cantidad de palabras anteriores y siguientes a considerar para formar un contexto. Por ejemplo, en el caso de _word0 **word1** **word2** WORD3 **word4** **word5** word6_, un contexto de WORD3 estaría formado por [_word1, word2, word4, word5_]).

Este caso se puede ejecutar con el siguiente comando:
	_python -i word-clustering.py_ (asegurar de que el archivo _resources/LaVanguardia.txt.gz_ fue descomprimido y que aparece el corpus LaVanguardia.txt)

Utilizando la técnica de umbral de frecuencia le matrix fue reducida desde el tamaño (126281,126281) al tamaño (126281,28877).

En el siguiente listado podemos ver todos los clusters con la cantidad de palabaras en cada uno:
	
	Cluster0: 10
	Cluster1: 10
	Cluster2: 10

**Clustering sobre word embeddings neuronales**