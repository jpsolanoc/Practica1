#Metodo para cargar sentimientos.
def get_sentimientos(dato):
	sentimientos = open(dato)
	valores = {}
	dato ="";
	for linea in sentimientos:
		termino, valor = linea.split("\t")
		valores[termino] = int(valor)
		if(len(dato)==0):
			dato = termino 
		else:	
			dato = dato +","+ termino 
	return dato.split(',')

#Metodo para cargar Tweet
def cargar_tweets(rutaTwets):
	data = open(rutaTwets)
	import json
	ls=[]
	for line in data:	
		tweets = json.loads(line)
		try:
			twEntrada = tweets['text']
			ls.append(twEntrada)
		except Exception as e:
			e	
	return ls

#Metodo para evaluar los Tweet con los sentimientos.
def evaluarTweet(tweet,sentimiento):
	numeroSentmientos = 0
	for data_tweet in tweet:
		for data_sentimiento in sentimiento:
			if data_tweet==data_sentimiento:
				numeroSentmientos = numeroSentmientos + 1;
	return numeroSentmientos;


datoSent = "sentimientos.txt" #Ruta del archivo de sentimientos
senti = get_sentimientos(datoSent);


datoTews = "salida_tweets.json" #Ruta del archivo de tweets
listaTweet = cargar_tweets(datoTews)

for tweet in listaTweet:
	tweetSeleccionado = tweet;
	tweetLista = tweetSeleccionado.split()
	tweetEvaluado = evaluarTweet(tweetLista,senti);
	if tweetEvaluado != 0:
		print ("EL SIGUIENTE TWEET :" +  tweetSeleccionado + " TIENE UN SENTIMIENTO ASOCIADO DE: "  + str(tweetEvaluado))


		
