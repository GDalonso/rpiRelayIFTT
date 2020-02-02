from flask import Flask, render_template, request
from Adafruit_IO import Client

# Configuração do adafruit
adafruit_Username = "Dalonso"  # change to your username
adafruit_Key = "aio_ClzS14KFNXbYHWmoD7jmqr0qnbXf"  # change to your adafruit key
adafruit_Feed = "testrpi"  # change to the name of your feed
# Inicializa o cliente mqtt com minhas informações do adafruit
client = Client(username=adafruit_Username, key=adafruit_Key)
client.send(adafruit_Feed, "1on")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def submit():
    comando = request.form["comando"]
    print(comando)
    client.send(adafruit_Feed, comando)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
