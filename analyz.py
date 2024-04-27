import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import joblib


# data_values = [1021, 1021, 1087, 1113, 1141, 1214, 1207, 1317, 1355, 1418, 1292] # Данные о языке 
# data_values_training = [1021, 1021, 1087, 1113, 1141] # Данные для обучения модели
class Analyz:

    data_index = ''
    data_series = ''

    def __init__(self, lang_name: str, data_values: list, data_values_training: list, training_steps: int):
        self.lang_name = lang_name
        self.data_values = data_values
        self.data_values_training = data_values_training
        self.training_steps = training_steps


    def model_is(self):
        model_file_name = f'arima_model_{self.lang_name}.pkl'  # Создаем новое имя файла с учетом значения переменной

        # Проверяем, существует ли уже сохраненная модель
        try:
            model = joblib.load(model_file_name)
            print('model file exists')            
        except FileNotFoundError:
            model = None
            print('create model file')

        # Обучаем модель ARIMA на данных только если модель не была загружена
        if model is None:
            self.create_new_model(model_file_name)


    def create_new_model(self, model_file_name):
        data_index = pd.date_range(start='01-01-2020', periods=len(self.data_values_training), freq='M')
        data_series = pd.Series(self.data_values_training, index=data_index)
        model = ARIMA(data_series, order=(1, 1, 1))
        model_fit = model.fit()
        joblib.dump(model_fit, model_file_name)

        self.get_forecasts()


    def get_forecast(self):

        # Прогнозируем несколько значений вперед
        forecast = model_fit.forecast(steps=self.training_steps)
        # Добавляем предсказанные значения к оригинальному набору данных
        new_dates = pd.date_range(start='01-01-2020', periods=len(self.data_values) + len(forecast), freq='M')
        new_data = self.data_values.copy()
        new_data.extend(round(forecast, 0))

        self.print_data(forecast, new_data)


    def print_data(self, forecast, new_data):
        print("---")
        print("Predicted Job Opening for the next period:", list(forecast))
        print("---")
        print("new_data: ", new_data)
        print("---")

    