def make_forecasts():
    """
    Esta función llama al modelo entrenado y con
    los features que ya se crearon anteriormente
    realiza predicciones.

    El archivo es guardado en la ubicación:
    data_lake/business/forecasts/precios-diarios.csv.

    >>> import pandas as pd
    >>> df = pd.read_csv('data_lake/business/forecasts/precios-diarios.csv')
    >>> df.columns
    Index(['fecha', 'precio_real', 'pronostico'], dtype='object')


    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import numpy as np
    import pickle
    from sklearn.preprocessing import MinMaxScaler

    # Lectura features
    df = pd.read_csv("data_lake/business/features/precios_diarios.csv")

    X = df["precios_dias_anteriores"].values
    X = [i.strip("][").replace(",", "").split() for i in X]

    lista = list()
    for i in X:
        lista2 = list()
        for j in i:
            lista2.append(float(j))
        lista.append(lista2)

    X = lista
    y = df["precio_escalado"].values

    # lectura modelo
    loaded_model = pickle.load(open("src/models/precios-diarios.pkl", "rb"))

    len_train_data = round(len(df) * 0.85)
    len_test_data = round(len(df) * 0.15)

    P = 30

    y_scaled_m1 = loaded_model.predict(X[-len_test_data:])

    # Modelo para desnormalizar
    db = pd.read_csv("data_lake/business/precios_diarios.csv")
    scaler = MinMaxScaler()
    scaler.fit(np.array(db["precio"]).reshape(-1, 1))

    # Resultados desnormalizados
    y_m1 = scaler.inverse_transform([[u] for u in y_scaled_m1])
    y_m1 = [u[0] for u in y_m1]

    respuesta = pd.DataFrame(
        zip(
            db["fecha"].iloc[-len_test_data:].values,
            db["precio"].iloc[-len_test_data:].values,
            y_m1,
        ),
        columns=["fecha", "precio_real", "pronostico"],
    )

    respuesta.to_csv("data_lake/business/forecasts/precios-diarios.csv", index=False)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
