def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.

    """
    # raise NotImplementedError("Implementar esta función")
    
    import pandas as pd
    from matplotlib import pyplot as plt
    
    df = pd.read_csv('data_lake/business/precios-mensuales.csv', parse_dates=['fecha'])
    
    fig, axis = plt.subplots(figsize=(8,5))
    
    plt.plot(df['fecha'], df['precio'], linewidth=1.5)
    
    plt.savefig('data_lake/business/reports/figures/monthly_prices.png')


if __name__ == "__main__":
    make_monthly_prices_plot()
    
    import doctest

    doctest.testmod()
