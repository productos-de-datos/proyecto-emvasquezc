def make_daily_prices_plot():
    """
    Grafica una serie de tiempo con los precios diarios de la energía.
    El gráfico se guarda en formato .png en la siguiente ruta:
    data_lake/business/reports/figures/daily_prices.png.

    >>> import os
    >>> os.path.isfile('data_lake/business/reports/figures/daily_prices.png')
    True

    """
    # raise NotImplementedError("Implementar esta función")
    
    import pandas as pd
    from matplotlib import pyplot as plt
    
    df = pd.read_csv('data_lake/business/precios-diarios.csv', parse_dates=['fecha'])
    
    fig, axis = plt.subplots(figsize=(8,5))
    
    plt.plot(df['fecha'], df['precio'], linewidth=1.5)
    
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')


if __name__ == "__main__":
    make_daily_prices_plot()
    
    import doctest

    doctest.testmod()
