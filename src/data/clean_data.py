def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import os

    archivos = os.listdir('data_lake/raw')

    li = []

    for archivo in archivos:
        df_temp = pd.read_csv('data_lake/raw/' + archivo, dtype={'Fecha': str})
        li.append(df_temp)

    df = pd.concat(li, axis=0, ignore_index=True)

    df = df.set_index('Fecha').stack()
    df = df.reset_index().rename(columns={'Fecha': 'fecha', 'level_1': 'hora', 0: 'precio'})

    # Hora con formato HH
    df['hora'] = df['hora'].str.zfill(2)

    df.to_csv('data_lake/cleansed/precios-horarios.csv', index=False)
    


if __name__ == "__main__":
    clean_data()

    import doctest

    doctest.testmod()


