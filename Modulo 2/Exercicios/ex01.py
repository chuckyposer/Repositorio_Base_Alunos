from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Word"

@app.route("/sobre")
def sobre():
    return "Oooi, sou a Marcella e estou aprendendo Python na fábrica de programadores."

@app.route("/ola/<nome>")
def ola(nome):
    return f'Olá {nome}!!! Seja bem vindo(a)!'

@app.route("/dobro/<int:numero>")
def dobro(numero):
    return f"O dobro de {numero} é {numero*2}"





if __name__ == "__main__":
    app.run(debug=True)

