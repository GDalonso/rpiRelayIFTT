import RPi.GPIO as GPIO
import sys

def inicializaBoard():
    # inicializa o gpio da placa
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def definePinoComoSaida(numeroPino):
    # define um pino como saída
    GPIO.setup(numeroPino, GPIO.OUT)

def definePinoComoEntrada(numeroPino):
    # define um pino como entrada
    GPIO.setup(numeroPino, GPIO.IN)

def escreveParaPorta(numeroPino, estadoPorta):
    # escreve um estado para uma porta
    GPIO.output(numeroPino, estadoPorta)
