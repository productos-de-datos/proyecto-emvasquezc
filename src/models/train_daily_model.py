def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

    >>> import os
    >>> os.path.isfile('src/models/precios-diarios.pkl')
    True


    """
    # raise NotImplementedError("Implementar esta función")

    from sklearn.neural_network import MLPRegressor
    import pandas as pd
    import numpy as np
    import pickle

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

    len_train_data = round(len(df) * 0.85)

    np.random.seed(123456)

    H = 1  # Se escoge arbitrariamente

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
    )

    # Entrenamiento
    mlp.fit(X[0:len_train_data], y[0:len_train_data])

    # Pronostico
    mlp.predict(X)

    filename = "src/models/precios-diarios.pkl"

    pickle.dump(mlp, open(filename, "wb"))


if __name__ == "__main__":
    train_daily_model()

    import doctest

    doctest.testmod()
