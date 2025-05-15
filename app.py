from flask import Flask, request, jsonify, render_template
from modelo import predecir_tiempo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.json
    distancia = float(data['distancia'])
    velocidad = float(data['velocidad'])
    trafico = int(data['trafico'])
    clima = int(data['clima'])
    terreno = int(data['terreno'])

    resultado = predecir_tiempo(distancia, velocidad, trafico, clima, terreno)
    return jsonify({'tiempo_estimado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
