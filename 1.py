import numpy as np
from scipy.signal import square
import matplotlib.pyplot as plt

# Генерируем прямоугольный сигнал
t = np.linspace(0, 1, 1000, endpoint=False)
square_wave = square(2 * np.pi * 5 * t, duty=0.5)

# Отрисовываем сигнал
plt.plot(t, square_wave)
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('Прямоугольный сигнал')
plt.show()
