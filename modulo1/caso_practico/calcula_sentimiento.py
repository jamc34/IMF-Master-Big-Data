from sys import argv
import json
import os
import re

# Esta funcion carga el fichero sentimientos en un diccionario donde:
# clave: es la palabra o grupo de palabras in minusculas
# valor: es otro diccionario con las siguientes claves:
#     "valor": entero que representa el valor numerico de la palabra o grupo de palabras
#     "regex": expresion regular compilada para buscar la palabra o grupo de palabras en un texto
#     "esgrupo": booleano (True: es un grupo de palabras, False: es una palabra individual)
#     "termino": la palabra o grupo de palabras
def cargar_fichero_sentimientos(path):	
    valores = {}
    if os.path.exists(path):
	    fichero=open(path)
	    for linea in fichero:
	        termino,valor=linea.split("\t")
	        pattern="(?i)\\b"+termino+"\\b"
	        esgrupo=False
	        if len(linea.split(" "))>1:
	            esgrupo=True
	        valores[termino.lower()]={'valor':int(valor), 'regex':re.compile(pattern),'esgrupo':esgrupo, 'termino':termino}
	    fichero.close()
    else:
        print("El fichero ",path," no existe.")
    return valores

# Esta funcion carga el el campo 'text' de cada tweet en una lista, exlcuyendo aquellos que no tienen dicho campo o estan vacios.
def cargar_fichero_tweets(path):
    tweets=[]
    if os.path.exists(path):
        fichero=open(path)
        for linea in fichero:
            if linea == "\n":
                continue
            lineapy = json.loads(linea)
            if 'text' in lineapy: 
                tweets.append(lineapy['text'])
        fichero.close()
    else:
        print("El fichero ",path," no existe.")
    return tweets
        
# Esta funcion escanea un tweet (o parte de el) generando una lista de terminos, donde cada termino puede ser un grupo de palabras definido en el fichero de sentimientos, o una palabra individual.
# Argumentos:
#   tweet: tweet (o parte de el) que se desea escanear
#   grupos: lista con cada uno de los grupos de palabras encontrados en el fichero de sentimientos
#   lista_terminos: repositorio donde se almacenan los terminos encontrados
# Descripcion:
# Por cada tweet o parte de un tweet:
# Divide el tweet haciendo split por el primer grupo de palabras de "grupos".
# Si el resultado es > 1 ,significa que el grupo de palabras ha sido encontrado en el tweet. En ese caso se anade el tweet a la lista de terminos y se llama recursivamente a las partes que han resultado de la division para tratar de encontrar otros grupos en ellas
# Si el resultado es 1 significa que o bien no se ha encontrado, en cuyo caso seguimos buscando recursivamente, o el tweet es exactamente igual que el grupo de palabras, en cuyo caso anadimos el grupo a la lista
def parse_tweet_recursivo(tweet, grupos,lista_terminos):
    if len(grupos) == 0:
        lista_terminos.extend(re.split(r"\W+",tweet))
        return
    grupo= grupos.pop()
    restos=grupo["regex"].split(tweet)
    if len(restos) == 1:
        if len(restos[0]) == len(tweet): 
            # group not found 
            parse_tweet_recursivo(tweet, grupos,lista_terminos)
        else:
            # group found at the beginning or the end   
            if grupo["regex"].match(tweet):
                lista_terminos.append(grupo["termino"])
                parse_tweet_recursivo(restos[0], grupos,lista_terminos)
            else: 
                parse_tweet_recursivo(restos[0], grupos,lista_terminos)
                lista_terminos.append(grupo["termino"])
    else: 
        # group found one or more times in the middle, leaving two or more parts
        notfirst=False
        for resto in restos:
            if notfirst:
                lista_terminos.append(grupo["termino"])
            parse_tweet_recursivo(resto, grupos,lista_terminos)
            notfirst=True

# Esta funcion recibe como parametros un tweet y una lista de grupos de palabras y divide el tweet en una lista donde cada elemento es:
# - uno de los grupos de palabras en "grupos" si se ha encontrado dicho grupo en el tweet
# - una palabra individual
def parse_tweet(tweet, grupos):
    lista_terminos=[]
    parse_tweet_recursivo(tweet, grupos, lista_terminos)
    return lista_terminos

# Esta funcion devuelve el subconjunto de los elementos en el fichero de sentimientos que son grupos de palabras (y no palabras individuales)     
def get_grupos(valores):
    return list(filter( lambda x: x["esgrupo"], valores.values()));

# Esta funcion recibe la lista de los tweets a procesar y la lista de los terminos en el fichero de sentimientos con sus valores y calcula el valor de cada tweet.
# El argumento formato puede tomar los siguientes valores "ejercicio1" o "ejercicio", de forma que imprimira el resultado de acuerdo a los requerimientos de los ejercicios 1 o 2 del caso practico.
def valorar_tweets(tweets, valores, formato):
    grupos_repo = get_grupos(valores)
    for tweet in tweets:
        grupos=grupos_repo.copy()
        valor_tweet = 0    
        lista_terminos=parse_tweet(tweet, grupos)
        for t in lista_terminos:
            if t.lower() in valores:
                valor_tweet += valores[t.lower()]["valor"]
        if formato == 'ejercicio1':
            print("EL SIGUIENTE TWEET: '", tweet, "' TIENE UN SENTIMIENTO ASOCIADO DE: ", valor_tweet)            
        elif formato == 'ejercicio2':
            for t in lista_terminos:
                if t.lower() not in valores:
                    print( t, ": ", valor_tweet )

# Funcion principal
path_fichero_tweets=argv[1]
path_fichero_sentimientos=argv[2]
valores=cargar_fichero_sentimientos(path_fichero_sentimientos)
tweets=cargar_fichero_tweets(path_fichero_tweets)

if 'ejercicio1' in argv:
    valorar_tweets(tweets, valores, 'ejercicio1')
elif 'ejercicio2' in argv:
    valorar_tweets(tweets, valores, 'ejercicio2')
else:
    print("Formato: python3.6 calcula_sentimiento.py <Fichero tweets> <Fichero sentimientos> [ejercicio1|ejercicio2]")
    

