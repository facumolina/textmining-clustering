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
Para normalizar las palabras se dividió el texto en sentencias y para cada sentencia, se creó una lista de tokens utilizando nltk. Luego, para cada lista de tokens
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

En el siguiente listado podemos ver las 10 palabras que más se relacionan con las palabras de los 20 primeros clusters:
	
	Cluster 0
	Most related words: per, i, el, és, més, com, dels, va, pel, tot

	Cluster 1
	Most related words: presidente, gobierno, ayer, ex, josé, asociación, dijo, según, ministro, josep

	Cluster 2
	Most related words: toda, ahora, aunque, tan, sido, vez, año, vida, mientras, do

	Cluster 3
	Most related words: casa, do, si, años, familia, blanca, nueva, toda, día, después

	Cluster 4
	Most related words: grupo, barcelona, empresa, presidente, año, años, españa, do, parte, compañía

	Cluster 5
	Most related words: tras, ayer, después, años, año, do, ser, sido, pasado, sólo

	Cluster 6
	Most related words: miguel, ángel, josé, juan, luis, director, san, según, martín, ayer

	Cluster 7
	Most related words: barcelona, i, joan, josé, sant, madrid, calle, josep, carlos, juan

	Cluster 8
	Most related words: do, tres, años, cuatro, grandes, toda, sólo, ayer, si, cinco

	Cluster 9
	Most related words: cada, vez, año, do, si, menos, ahora, años, mismo, toda

	Cluster 10
	Most related words: gobierno, siempre, dels, aunque, si, sido, política, casi, ley, pp

	Cluster 11
	Most related words: obra, además, autor, parte, sido, tan, menos, vida, obras, forma

	Cluster 12
	Most related words: ser, puede, sido, si, debe, pueden, aunque, do, tan, años

	Cluster 13
	Most related words: horas, director, canal, tele, antena, i, el, tres, años, después

	Cluster 14
	Most related words: así, bien, josé, menos, sino, españa, el, hoy, junto, nuevo

	Cluster 15
	Most related words: millones, peseta, año, dólares, do, años, dinero, ciento, total, pasado

	Cluster 16
	Most related words: ciudad, barcelona, centro, zona, gran, ayer, do, capital, toda, tan

	Cluster 17
	Most related words: si, do, años, ayer, sólo, ser, barcelona, ahora, parte, gobierno

	Cluster 18
	Most related words: día, cada, hoy, años, si, año, barcelona, después, siguiente, ser

	Cluster 19
	Most related words: tres, do, años, cuatro, ayer, sólo, si, año, grandes, veces

En el archivo _results/wordclustering.txt_ se puede ver output completo de la ejecución.

**Clustering sobre word embeddings neuronales**

Este caso se puede ejecutar con el siguiente comando:
	_python -i word2vec-and-clustering.py_ (asegurar de que el archivo _resources/LaVanguardia.txt.gz_ fue descomprimido y que aparece el corpus LaVanguardia.txt)

Utilizando esta técnica, la matriz generada tiene un tamaño de (126281, 100), mucho menor a la técnica anterior.

En el siguiente listado podemos ver algunas palabras de los 10 primeros clusters:

	Cluster 0
	Words: año, me, caso, catarara, ciclo, día, momento, tiempo, siendo, espacio, capítulo, bianual, programa, ambiente, punto, otoño, nombre, camino, bloque, campo, equipo, idolatrar, lugar, libro, teatro, escenario, destino, impares, heures, paso, patinazo, plano, siglo, título, puente, disco, periodo, plazo, oriente, término

	Cluster 1
	Words: peajes, titularidad, correspondientes, tarifas, concesionarias, incrementar, aplica, reducción, beneficie, mantenimiento, pagarán, cubrir, conexiones, eléctricas, previsión, clientela, mejora, techo, depósitos, suministro, producto, requisitos, específicos, usuario, lleguen, vender, mediante, generen, creciendo

	Cluster 2
	Words: pasillos, subsanado, mando, turno, hoja, bella, tensa, solitaria, atendida, cortada, terraza, mirador, suspendido, falda, sexto, aparecerá, recuperará, hundió, guifré, motivó, suspendió, desempeñaban, finalizaron, actuará, armado, retirado, concluyes, lampedusa, internado, aficionó, ópera, emperador, cabecera

	Cluster 3
	Words: días, horas, expirado, embucharon, deseasen, buyle, desapercibidas, caballeroso, aplazará, sato, solstice, arraigó, acristalado, encuadernada, identificarme, nuyum, crecerían, aconsejase, pórticos, algarve, graiera, úrico, terroir, hispanoguineana, colomense, reconociéndolo, minitenis, facturaciones, emte, nacían

	Cluster 4
	Words: gobierno, consejo, ministros, decreto, apruebe, ministro, piqué, aseguró, dado, críticas, catalán, marco, señala, nadal, psc, expresó, recordó, pendiente, general, afirmar, añadió, aprovechó, mantiene, anuncio, tomada, nota, dijo, respondió, alarmista, dirigentes, debate, voto, públicamente, señalar, carta, ciu, pp

	Cluster 5
	Words: aprobó, explicó, fuentes, reveló, vanguardia, responsables, informe, indicativas, datos, director, policial, manifestaron, prensa, diario, consta, informa, seskutov, anunciaron, indicaron, informaron, xxvii, reunieron, campaners, denunció, bromeaba, relató, cruzarla, desmantelado, encuesta, anunció, fayos, confirmó

	Cluster 6
	Words: decidió, debía, iba, cuenta, podía, preferido, decidido, puede, pudo, debe, va, puedan, pueden, quiso, quiere, acaban, arrollado, van, pasa, permitió, empezado, podría, pretende, poder, deberá, podrían, obliga, volvieron, vamos, debería, devoradas, volvió, dejó, deja, capaz, quería, suele, retrocedería, gustado,  

	Cluster 7
	Words: cubrieron, universitària, begues, climent, associats, sl, recalificación, tractament, residus, sa, trm, coberta, pallejà, magda, cal, patronatos, siurana, ter, alfons, hortelanos, roda, vilassar, german, noguera, rubió, cáritas, món, ajuda, psicopatològica, psicosocial, immigrant, de, impulsoras, wave, propietario

	Cluster 8
	Words: misma, cada, única, gran, primera, cuya, toda, tal, aquella, mayor, larga, menor, alguna, doble, urbana, segunda, plenum, propia, leídas, buena, cualquier, última, civil, pequeña, alta, principal, puesta, férrea, cuarta, tercera, ninguna, avanzada, forman, acuerdas, depure, tirarse, formará, bobies, original, formaba

	Cluster 9
	Words: quedan, alteraciones, intensidad, gotas, menos, male, causa, semáforos, dan, moda, amantes, verdades, relatos, arma, solamente, motivos, ponernos, aquellos, situaciones, ejemplos, recomendable, evitan, cola, marchan, sufriendo, chavales, perros, excrementos, ponen, pasos, motivaron, admiten, aficionado, incapacitados

En el archivo _results/word2vecclustering.txt_ se puede ver output completo de la ejecución.


