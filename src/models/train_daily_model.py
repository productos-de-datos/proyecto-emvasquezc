def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    # raise NotImplementedError("Implementar esta función")
    
    from sklearn.neural_network import MLPRegressor
    from features.make_features import make_features
    
    X, observed_scaled = make_features()

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
    mlp.fit(X[0:len_train_data], observed_scaled[0:len_train_data])  # 239 - 24 = 215

    # Pronostico
    y_scaled_m1 = mlp.predict(X)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
