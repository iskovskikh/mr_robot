

import plotly.graph_objects as go
import pandas as pd

from settings.base import BASE_DIR

df = pd.read_csv(BASE_DIR.parent / 'finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'], high=df['AAPL.High'],
                low=df['AAPL.Low'], close=df['AAPL.Close'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)


# fig.show()
#
# import plotly.graph_objects as go
#
# # Данные для графика
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]  # простые числа
#
# # Создание графика
# fig = go.Figure()
#
# # Добавление линии
# fig.add_trace(go.Scatter(
#     x=x,
#     y=y,
#     mode='lines+markers',  # Линия + маркеры
#     name='Простое число',
#     line=dict(color='blue', width=2)
# ))
#
# # Настройка макета
# fig.update_layout(
#     title='Пример графика с Plotly',
#     xaxis_title='X-ось',
#     yaxis_title='Y-ось'
# )


# import plotly.io as pio
# pio.renderers.default = 'browser'

# Показать график
# fig.show()

fig.write_html("plot.html")  # Создаёт файл
import webbrowser
webbrowser.open("plot.html")  # Открывает в браузере