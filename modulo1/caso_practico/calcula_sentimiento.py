from sys import argv
import json
import os
import re

def load_fichero_sentimientos(path):	
    valores = {}
    if os.path.exists(path):
	    fichero=open(path)
	    for linea in fichero:
	        termino,valor=linea.split("\t")
	        pattern="\W"+termino+"\W"
	        valores[termino]={'valor':int(valor), 'regex': re.compile(pattern,re.IGNORECASE)}
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
        for termino, termdata in valores.items():
            if termdata['regex'].search(tweet) != None:
                valor_tweet+=termdata['valor']
                print("Encontrado termino ", termino, " en tweet: ", tweet, " con valor ", termdata['valor'])
        print("EL SIGUIENTE TWEET: '", tweet, "' TIENE UN SENTIMIENTO ASOCIADO DE: ", valor_tweet)            

# No tiene en cuenta grupos de palabras
def valorar_tweets_fast(tweets, valores):
    for tweet in tweets:
        valor_tweet = 0    
        words=re.split(r'\W+',tweet)
        for word in words:
            if word in valores:
                valor_tweet+=valores[word]['valor']
                print("Encontrado termino ", word, " en tweet: ", tweet, " con valor ", valores[word]['valor'])
        print("EL SIGUIENTE TWEET: '", tweet, "' TIENE UN SENTIMIENTO ASOCIADO DE: ", valor_tweet)            

path_fichero_tweets=argv[1]
path_fichero_sentimientos=argv[2]
options=[]
if len(argv) > 3:
    options_string=argv[3]
    options=re.split(',',options_string)


valores=load_fichero_sentimientos(path_fichero_sentimientos)
tweets=load_fichero_tweets(path_fichero_tweets)
# print("Tweets: ", tweets );
# print ("Valores: ", valores.items())
if 'fast' in options:
    print("Do it fast")
    valorar_tweets_fast(tweets, valores)
else:
    print("Do it well")
    valorar_tweets(tweets, valores)


