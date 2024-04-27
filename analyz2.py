import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import joblib

class Analyz:

    data_index = ''
    data_series = ''

    def __init__(self, training_steps: int, time_start: str):
        self.training_steps = training_steps
        self.time_start = time_start

    
    def analyze(self, lang_name: str, data_values: list, data_values_training: list, training_steps: int):

        # Создаем временной ряд из данных
        data_index = pd.date_range(start=self.time_start, periods=len(data_values_training), freq='M')
        data_series = pd.Series(data_values_training, index=data_index)

        # Обучаем модель ARIMA на данных
        model = ARIMA(data_series, order=(1, 1, 1))  # Пример параметров модели (p=1, d=1, q=1)
        model_fit = model.fit()

        # Прогнозируем несколько значений вперед (например, 3 значения)
        forecast = model_fit.forecast(steps=self.training_steps)
        print("Predicted Job Opening for the next period:", forecast)
        print("Predicted Job Opening for the next period:", forecast[0])

        # Добавляем предсказанные значения к оригинальному набору данных
        new_dates = pd.date_range(start=self.time_start, periods=len(data_values) + len(forecast), freq='M')
        new_data = data_values.copy()
        new_data.extend(round(forecast, 0))

        #Визуализация новых данных
        plt.figure(figsize=(5, 4))
        plt.plot(data_index, data_values, marker='o', label='Оригинальные данные')
        plt.plot(new_dates, new_data, marker='x', linestyle='dashed', color='red', label='Прогноз')
        plt.xlabel('Дата')
        plt.ylabel('Значение')
        plt.title('Прогноз значений временного ряда')
        plt.legend()
        plt.show()

        return new_data

    