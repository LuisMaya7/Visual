import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]


plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, color='blue')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Matemáticas')
plt.ylabel('Ciencias')
plt.show()

materias = ['Matemáticas', 'Ciencias', 'Literatura']

plt.figure(figsize=(8, 6))
plt.errorbar(materias, [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)],
             yerr=np.array([errores_matematicas, errores_ciencias, errores_literatura]).T, fmt='o', capsize=10)
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificación Promedio')
plt.legend(['Promedio'])
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(matematicas, bins=10, color='purple', edgecolor='black')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.show()
