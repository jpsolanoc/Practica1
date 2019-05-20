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
def evaluarSentimiento(tweet,sentimiento):
	con = 1;
	for palabra in tweet:
		if 	evaluaPalabra(palabra,sentimiento) == False:
			print (palabra +"\t"+ str (round(con/len(tweet),1)))
		con = con + 1;			

#Metodo para evaluar si la palabra dentro del tweet se encuentra en el archivo de sentimientos.
def evaluaPalabra (palabra,sentimiento):
	for data_sentimiento in sentimiento:
		if palabra == data_sentimiento:
			return True;
			break;
	return False;


datoSent = "sentimientos.txt" #Ruta del archivo de sentimientos
senti = get_sentimientos(datoSent);


datoTews = "salida_tweets.json" #Ruta del archivo de tweets
listaTweet = cargar_tweets(datoTews)

#Recorrido de los Tweets 
for tweet in listaTweet:
	tweetSeleccionado = tweet;
	tweetLista = tweetSeleccionado.split()
	evaluarSentimiento(tweetLista,senti);
	


		
