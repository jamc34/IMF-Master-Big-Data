from sys import argv
import json
import os
import re

# Version 1 

def load_fichero_sentimientos(path):	
    valores = {}
    if os.path.exists(path):
	    fichero=open(path)
	    for linea in fichero:
	        termino,valor=linea.split("\t")
	        valores[termino]=int(valor)
	    fichero.close()
    else:
        print("El fichero ",path," no existe.")
    return valores

def load_fichero_tweets(path):
    tweets=[]
    if os.path.exists(path):
        fichero=open(path)
        for linea in fichero:
            if linea == "\n":
                continue
            lineapy = json.loads(linea)
            if 'text' in lineapy: 
                # print("Text found: ",lineapy['text'])
                tweets.append(lineapy['text'])
        fichero.close()
    else:
        print("El fichero ",path," no existe.")
    return tweets
        
def valorar_tweets(tweets, valores):
    for tweet in tweets:
        valor_tweet = 0    
        for termino in valores:
            if reg.search(termino, tweet) != None:
                valor_tweet+=valores[termino]
                print("Encontrado termino ", termino, " en tweet: ", tweet, " con valor ", valores[termino])
        print("EL SIGUIENTE TWEET: '", tweet, "' TIENE UN SENTIMIENTO ASOCIADO DE: ", valor_tweet)            

path_fichero_tweets=argv[1]
path_fichero_sentimientos=argv[2]

valores=load_fichero_sentimientos(path_fichero_sentimientos)
tweets=load_fichero_tweets(path_fichero_tweets)
# print("Tweets: ", tweets );
# print ("Valores: ", valores.items())
valorar_tweets(tweets, valores)
