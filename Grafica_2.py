import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas',
                'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia',
                'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias',
                'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí',
                 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.boxplot([df[df['materia'] == materia]['nota'] for materia in df['materia'].unique()],
            labels=df['materia'].unique())
plt.title('Distribución de Notas por Materia')
plt.xlabel('Materias')
plt.ylabel('Notas')
plt.grid(True)
plt.show()

colors = ['c', 'firebrick']
startangle= 45
plt.pie(df['aprobado'].value_counts(), labels=['Aprobados', 'No Aprobados'], autopct='%1.1f%%', colors=colors, startangle=startangle)
plt.title('Distribución de Aprobados y No Aprobados')
plt.show()

