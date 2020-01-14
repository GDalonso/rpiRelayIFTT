from Adafruit_IO import Client, MQTTClient
from gpiControl import inicializaBoard, definePinoComoSaida, escreveParaPorta

# setup de portas gpio
inicializaBoard()
#Relay 1
definePinoComoSaida(11)
#Relay 2
definePinoComoSaida(12)

# aio = Client(username='Dalonso', key='aio_ClzS14KFNXbYHWmoD7jmqr0qnbXf')
# aio.send('testrpi', randint(0,50))


def connected(client):
	adafruit_Feed='testrpi' #change to the name of your feed
	client.subscribe(adafruit_Feed)

def message(client, feed_id, payload):
	print(payload)
	if payload.lower() == '1on':
		escreveParaPorta(11,0)
	elif payload.lower() == '1off':
		escreveParaPorta(11,1)
	elif payload.lower() == '2on':
		escreveParaPorta(12,0)
	elif payload.lower() == '2off':
		escreveParaPorta(12,1)
	else:
		print("relay ainda ainda não implementado")


adafruit_Username='Dalonso' #change to your username
adafruit_Key='aio_ClzS14KFNXbYHWmoD7jmqr0qnbXf' #change to your adafruit key
client = MQTTClient(username=adafruit_Username, key=adafruit_Key)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_message    = message

client.connect()

# pick one of the following 3 ways of looping the MQTT client
# client.loop_background() # start background thread and return
# client.loop() # loop once
client.loop_blocking() # block forever on client loop