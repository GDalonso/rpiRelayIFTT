# rpiRelayIFTT
Controle de um relay com uma raspberry pi via google assistant e IFTT usando Adafruit.io, MQTT e RPI.GPIO


Setup
- criar conta no adafruit.io
- criar um feed
- definir variáveis adafruit_Username com username e adafruit_Key com a key do seu projeto
- criar conta IFTTT
- Criar um applet
- This : Google assistant, phrase with a number
- Turn on relay number # - # denota a variável de número da google assistant
- escrever {{NumberField}}on pro feed que vc criou
- fazer os dois passos anteriores pra off
- colocar o nome do feed na variável adafruit_Feed 
- python3 adafruit.py

Tutoriais usados
Adafruit - Criando filas e dashboards https://www.youtube.com/watch?v=IfzpoFGkmns
Adafruit - Integração via python com fila e IFTT https://www.reddit.com/r/raspberry_pi/comments/5p1p35/short_guide_on_using_adafruitio_and_ifttt_with/
