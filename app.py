from flask import Flask

from analyz2 import Analyz

app = Flask(__name__)

@app.route('/')#/api/flask
def hello_world():
    return 'This is from Flask Serverless Function'

@app.route('/analyz')
def getAnalyz():

    lang_name = 'php'
    training_steps = 1

    # data_values =          [1021, 1021, 1087, 1113, 1141]
    # data_values_training = [1214, 1207, 1317, 1355, 1418]  # Данные для обучения модели
    
    data_values =          [1021, 1021, 1087, 1113, 1141, 1214, 1207, 1317, 1355, 1418, 1292]
    data_values_training = [1021, 1021, 1087, 1113, 1141, 1214, 1207, 1317, 1355, 1418, 1292] # Данные для обучения модели


    analyz = Analyz(training_steps, '01-01-2020')    
    return analyz.analyze(lang_name, data_values, data_values_training, training_steps)

if __name__ == '__main__':
    app.run()