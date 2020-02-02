from Adafruit_IO import Client, MQTTClient
from gpiControl import inicializaBoard, definePinoComoSaida, escreveParaPorta

# Colocar aqui o número físico das portas que pretende usar como saída
# portas - ["relay1", "relay2", "LED"]
portas_em_uso = [11, 12, 15]

# Configuração do adafruit
adafruit_Username = "Dalonso"  # change to your username
adafruit_Key = "aio_ClzS14KFNXbYHWmoD7jmqr0qnbXf"  # change to your adafruit key
adafruit_Feed = "testrpi"  # change to the name of your feed

# como mandar data para um feed
# aio.send('testrpi', randint(0,50))

# setup de portas gpio
inicializaBoard()
for porta in portas_em_uso:
    definePinoComoSaida(porta)


def connected(client):
    client.subscribe(adafruit_Feed)


def message(client, feed_id, payload):
    print(payload)
    payload = payload.replace(" ", "").replace("the", "")
    if payload.lower() == "1on":
        escreveParaPorta(11, 0)
    elif payload.lower() == "1off":
        escreveParaPorta(11, 1)
    elif payload.lower() == "2on":
        escreveParaPorta(12, 0)
    elif payload.lower() == "2off":
        escreveParaPorta(12, 1)
    # tá invertido por motivos de LED faz mais sentido que relay
    elif payload.lower() == "3on":
        escreveParaPorta(15, 1)
    elif payload.lower() == "3off":
        escreveParaPorta(15, 0)
    else:
        print("relay ainda ainda não implementado")


# Inicializa o cliente mqtt com minhas informações do adafruit
client = MQTTClient(username=adafruit_Username, key=adafruit_Key)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_message = message

client.connect()

# pick one of the following 3 ways of looping the MQTT client
# client.loop_background() # start background thread and return
# client.loop() # loop once
client.loop_blocking()  # block forever on client loop
