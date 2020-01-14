from flask import Flask, render_template, request
from gpiControl import inicializaBoard, definePinoComoSaida, escreveParaPorta

app = Flask(__name__)

# setup de portas gpio
inicializaBoard()
#Relay 1
definePinoComoSaida(11)
#Relay 2
definePinoComoSaida(12)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)

    if(comando == '1ON'):
       escreveParaPorta(11,0) 
    elif(comando == '1OFF'):
       escreveParaPorta(11,1)
    elif(comando == '2ON'):
       escreveParaPorta(12,0)
    elif(comando == '2OFF'):
       escreveParaPorta(12,1)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
