def make_features():
    """
    Esta función extrae las características necesarias para 
    realizar el entrenamiento del modelo.
    
    El archivo es guardado en data_lake/business/features/precios-diarios.csv.

    >>> import pandas as pd
    >>> df = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    >>> df.columns
    Index(['fecha', 'precios_dias_anteriores', 'precio_escalado'], dtype='object')


    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    df = pd.read_csv(
        "data_lake/business/precios_diarios.csv",
        parse_dates=["fecha"],
        index_col=["fecha"],
    )

    #
    # Como primer paso se escala la serie al intervalo [0, 1]
    # ya que esto facilita el entrenamiento del modelo
    #
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler

    len_train_data = round(len(df) * 0.85)

    # crea el transformador
    scaler = MinMaxScaler()

    # escala la serie
    data_scaled = scaler.fit_transform(np.array(df["precio"]).reshape(-1, 1))

    # z es un array de listas como efecto
    # del escalamiento
    data_scaled = [u[0] for u in data_scaled]

    P = 30

    X = []
    for t in range(P - 1, len(df) - 1):
        X.append([data_scaled[t - n] for n in range(P)])

    observed_scaled = data_scaled[P:]

    features = pd.DataFrame(
        zip(df.iloc[P:].index, X, observed_scaled),
        columns=["fecha", "precios_dias_anteriores", "precio_escalado"],
    )

    features.to_csv("data_lake/business/features/precios-diarios.csv", index=False)


if __name__ == "__main__":
    make_features()

    import doctest

    doctest.testmod()
