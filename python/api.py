from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Predicciones de Iris'

@app.route('/predict')
def predict():
    return 'Proximamente prediccion!'

@app.route('/add_data')
def hello():
    return 'Ingreso de datos nuevos'


if __name__ == "__main__":
    app.run()