# rpiRelayIFTT
Controle de um relay com uma raspberry pi via google assistant e IFTT usando Adafruit.io, MQTT e RPI.GPIO


## Setup

### Adafruit.io
- criar conta no adafruit.io
- criar um feed
- definir variáveis adafruit_Username com username e adafruit_Key com a key do seu projeto
- `sudo pip3 install adafruit-io`

### IFTTT
- Criar um applet
- This : Google assistant -> say a phrase with both a number and a text ingredient
- Turn relay number # $ 
    - '#' variável de número da google assistant, diga o número do relay
    - '$' variável de texto da google assistant, diga on ou off
- escrever {{NumberField}}{{TextField}} pro feed do adafruit que vc criou
- colocar o nome do feed na variável adafruit_Feed 

- python3 adafruit.py

Tutoriais usados
Adafruit - Criando filas e dashboards https://www.youtube.com/watch?v=IfzpoFGkmns
Adafruit - Integração via python com fila e IFTT https://www.reddit.com/r/raspberry_pi/comments/5p1p35/short_guide_on_using_adafruitio_and_ifttt_with/
