import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Carga los archivos de datos
df_sandra = pd.read_csv('sandraTorres.csv')
df_bernardo = pd.read_csv('bernardoArevalo.csv')

# Inicializa la aplicación Dash
app = dash.Dash(__name__)

# Define el layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard interactivo de Candidatos Presidenciales"),
    
    # Botones para seleccionar el candidato
    dcc.RadioItems(
        id='selector-candidato',
        options=[
            {'label': 'Sandra Torres', 'value': 'sandra'},
            {'label': 'Bernardo Arevalo', 'value': 'bernardo'}
        ],
        value='sandra',  # Candidato por defecto
        labelStyle={'display': 'block'}
    ),
    
    # Gráficos enlazados para mostrar información de retweets y likes
    html.Div([
        dcc.Graph(id='grafico-retweets', className='grafico'),
        dcc.Graph(id='grafico-likes', className='grafico'),
    ], className='graficos-container'),
    
])

# Función para ordenar el DataFrame en función del recuento (retweets o likes)
def ordenar_df_por_recuento(df, columna_recuento, ascendente=True):
    return df.sort_values(by=columna_recuento, ascending=ascendente)

# Callback para actualizar los gráficos en función del candidato seleccionado
@app.callback(
    [Output('grafico-retweets', 'figure'),
     Output('grafico-likes', 'figure')],
    Input('selector-candidato', 'value')
)
def actualizar_graficos(candidato):
    if candidato == 'sandra':
        df = df_sandra
        titulo_retweets = 'Recuento de Retweets para Sandra Torres'
        titulo_likes = 'Recuento de Likes para Sandra Torres'
    else:
        df = df_bernardo
        titulo_retweets = 'Recuento de Retweets para Bernardo Arevalo'
        titulo_likes = 'Recuento de Likes para Bernardo Arevalo'



if _name_ == '_main_':
    app.run_server(debug=True, port=8054)
