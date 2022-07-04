def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



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
