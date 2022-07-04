def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



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
