def compute_monthly_prices():
    """
    Esta función toma los precios por hora por día y los promedia
    en un solo mes. Las columnas del DataFrame son:
    fecha (YYYY-MM) y precio.

    El nuevo archivo se guarda en la ruta data_lake/business/precios-mensuales.csv.
   

    >>> import pandas as pd
    >>> df = pd.read_csv('data_lake/business/precios-mensuales.csv', \
    parse_dates=['fecha'], index_col=['fecha'])
    >>> pd.infer_freq(df.index)
    'MS'

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv',
    parse_dates=['fecha'])

    df['fecha'] = df['fecha'].dt.to_period('M')

    avg_month = df.groupby('fecha')['precio'].mean()

    avg_month.to_csv('data_lake/business/precios-mensuales.csv')


if __name__ == "__main__":
    compute_monthly_prices()


    import doctest

    doctest.testmod()
