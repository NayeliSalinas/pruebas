import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (puedes mejorarlos)
data = [
    [10, 60, 2, 0, 0, 12],
    [15, 40, 5, 1, 1, 30],
    [20, 70, 1, 0, 0, 18],
    [8, 30, 8, 2, 1, 40],
    [50, 100, 3, 0, 0, 35],
]

X = [d[:5] for d in data]
y = [d[5] for d in data]

model = LinearRegression()
model.fit(X, y)

def predecir_tiempo(distancia, velocidad, trafico, clima, terreno):
    entrada = np.array([[distancia, velocidad, trafico, clima, terreno]])
    return round(model.predict(entrada)[0], 2)
