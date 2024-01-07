import pandas as pd
import plotly.express as px

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

fig_boxplot = px.box(df, x='materia', y='nota', color='materia', 
                     title='Grafico de cajas',
                     labels={'nota': 'Valores'},
                     category_orders={'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']},
                     color_discrete_sequence=px.colors.qualitative.Set2)


fig_boxplot.update_layout(xaxis_title='Materia', yaxis_title='Nota')

fig_boxplot.show()

fig_pie_chart = px.pie(df, df['aprobado'], title='Grafico de torta')

fig_pie_chart.show()
