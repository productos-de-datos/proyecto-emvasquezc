def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    # raise NotImplementedError("Implementar esta función")
    
    import pandas as pd
    
    df = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    
    
    #
    # Como primer paso se escala la serie al intervalo [0, 1]
    # ya que esto facilita el entrenamiento del modelo
    #
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler

    # Definir cantidad de datos para entrenamiento y test
    len_train_data = round(len(df)*0.85)
    len_test_data = round(len(df)*0.15)

    # crea el transformador
    scaler = MinMaxScaler()

    # escala la serie
    data_scaled = scaler.fit_transform(np.array(df['precio']).reshape(-1, 1))

    # z es un array de listas como efecto
    # del escalamiento
    data_scaled = [u[0] for u in data_scaled]
    
    
    P = 30

    X = []
    for t in range(P - 1, len(df) - 1):
        X.append([data_scaled[t - n] for n in range(P)])

    observed_scaled = data_scaled[P:]
    
    return X, observed_scaled


if __name__ == "__main__":
    import doctest

    doctest.testmod()
