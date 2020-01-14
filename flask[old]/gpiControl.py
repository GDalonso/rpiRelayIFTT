import RPi.GPIO as GPIO
import sys

def inicializaBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def definePinoComoSaida(numeroPino):
    GPIO.setup(numeroPino, GPIO.OUT)

def escreveParaPorta(numeroPino, estadoPorta):
    GPIO.output(numeroPino, estadoPorta)
