def compute_daily_prices():
    """
    Esta función toma los precios por hora por día y los promedia
    en un solo día. Las columnas del DataFrame son:
    fecha (YYYY-MM-DD) y precio.

    El nuevo archivo se guarda en la ruta data_lake/business/precios-diarios.csv.
   
    >>> import pandas as pd
    >>> df = pd.read_csv('data_lake/business/precios-diarios.csv', \
    parse_dates=['fecha'], index_col=['fecha'])
    >>> pd.infer_freq(df.index)
    'D'

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')

    avg_daily = df.groupby('fecha')['precio'].mean()

    avg_daily.to_csv('data_lake/business/precios-diarios.csv')


if __name__ == "__main__":
    compute_daily_prices()

    import doctest

    doctest.testmod()
