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

Utilizando la técnica de umbral de frecuencia la matriz fue reducida desde el tamaño (126281,126281) al tamaño (126281,28877).

En el siguiente listado podemos ver todos los clusters con la cantidad de palabaras en cada uno:
	
	Cluster#0 - Total words: 121
	Cluster#1 - Total words: 74525
	Cluster#2 - Total words: 1027
	Cluster#3 - Total words: 2076
	Cluster#4 - Total words: 9825
	Cluster#5 - Total words: 676
	Cluster#6 - Total words: 1163
	Cluster#7 - Total words: 1479
	Cluster#8 - Total words: 1057
	Cluster#9 - Total words: 730
	Cluster#10 - Total words: 1067
	Cluster#11 - Total words: 1083
	Cluster#12 - Total words: 1440
	Cluster#13 - Total words: 1517
	Cluster#14 - Total words: 399
	Cluster#15 - Total words: 1480
	Cluster#16 - Total words: 1861
	Cluster#17 - Total words: 1282
	Cluster#18 - Total words: 1435
	Cluster#19 - Total words: 854
	Cluster#20 - Total words: 719
	Cluster#21 - Total words: 1389
	Cluster#22 - Total words: 492
	Cluster#23 - Total words: 909
	Cluster#24 - Total words: 922
	Cluster#25 - Total words: 1270
	Cluster#26 - Total words: 846
	Cluster#27 - Total words: 984
	Cluster#28 - Total words: 767
	Cluster#29 - Total words: 670
	Cluster#30 - Total words: 800
	Cluster#31 - Total words: 1992
	Cluster#32 - Total words: 1019
	Cluster#33 - Total words: 1938
	Cluster#34 - Total words: 845
	Cluster#35 - Total words: 2328
	Cluster#36 - Total words: 1116
	Cluster#37 - Total words: 1050
	Cluster#38 - Total words: 410
	Cluster#39 - Total words: 718

**Clustering sobre word embeddings neuronales**