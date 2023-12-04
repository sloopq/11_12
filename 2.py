import numpy as np
import matplotlib.pyplot as plt

# Генерируем данные с нормальным распределением
mean = 0
std_dev = 1
data = np.random.normal(mean, std_dev, 1000)

# Отрисовываем гистограмму
plt.hist(data, bins=30, density=True, alpha=0.7, color='blue')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')
plt.title('Нормальное распределение')
plt.show()
