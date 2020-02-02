import RPi.GPIO as GPIO
import sys


def inicializaBoard():
    # inicializa o gpio da placa
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)


def definePinoComoSaida(numeroPino):
    # define um pino como saída
    """
    O default está high pq os controles do Relay são invertidos, High é desligado e Low é ligado
    por algum motivo bizarro que ninguém entende
    Alterar isso pra lidar com qualquer outro equipamento normal
    """
    GPIO.setup(numeroPino, GPIO.OUT, initial=GPIO.HIGH)
    pass


def definePinoComoEntrada(numeroPino):
    # define um pino como entrada
    GPIO.setup(numeroPino, GPIO.IN)


def escreveParaPorta(numeroPino, estadoPorta):
    # escreve um estado para uma porta
    GPIO.output(numeroPino, estadoPorta)
