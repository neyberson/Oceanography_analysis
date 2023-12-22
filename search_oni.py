def search_oni(anomalia, data):
    if anomalia == 'positivo':
        oni = data.loc[data['ANOM'].between(0.01, 3), 'ANOM']
    elif anomalia == 'negativo':
        oni = data.loc[data['ANOM'].between(-3, -0.01), 'ANOM']
    elif anomalia == 'neutro':
        oni = data.loc[data['ANOM'] == 0, 'ANOM']
    else:
        oni = None # opcional: puedes añadir un caso por si la anomalía no es válida
    return oni