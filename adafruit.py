from Adafruit_IO import *
from random import randint

aio = Client(username='Dalonso', key='aio_ClzS14KFNXbYHWmoD7jmqr0qnbXf')

for i in range(100):
	aio.send('testrpi', randint(0,50))
	