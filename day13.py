import numpy as np
import matplotlib.pyplot as plt

def f1(i1, i3):
    return -20 * i1 + 10 * i3 + 100

def f3(i1, i3):
    return 10 * i1 - 20 * i3

h = 0.01
i1 = 0
i3 = 0
times = [0]
i1_values = [i1]
i3_values = [i3]

for t in np.arange(0, 5, h):
    # Predicción
    k1_i1 = i1+h*f1(i1, i3)
    k1_i3 = i3+h*f3(i1, i3)

    # Evaluación de las derivadas en el punto intermedio
    k2_i1 = f1(k1_i1,k1_i3)
    k2_i3 = f3(k1_i1,k1_i3)

    # Cálculo de los nuevos valores
    i1 += h * (f1(i1,i3) + k2_i1) / 2
    i3 += h * (f3(i1,i3) + k2_i3) / 2

    print(i1,i3)

    times.append(t + h)
    i1_values.append(i1)
    i3_values.append(i3)

plt.plot(times, i1_values, label="i1(t)")
plt.plot(times, i3_values, label="i3(t)")
plt.xlabel("Time (t)")
plt.ylabel("Current")
plt.legend()
plt.show()
