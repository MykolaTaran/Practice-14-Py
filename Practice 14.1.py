import numpy as np
import matplotlib.pyplot as plt

# Визначення функції Y(x)
def Y(x):
    return (1/x) * np.cos(x**2 + 1/x)

# Генерація значень x в діапазоні [1, 10]
x_values = np.linspace(1, 10, 1000)

# Обчислення відповідних значень Y(x)
y_values = Y(x_values)

# Побудова графіка
plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=2, label=r'$\frac{1}{x} \cos\left(x^2 + \frac{1}{x}\right)$')

# Позначення осей
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Виведення назви графіка
plt.title('Графік функції Y(x)')

# Виведення легенди
plt.legend()

# Відображення графіка
plt.show()