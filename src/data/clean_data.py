def clean_data():
    """
    Esta función une todos los años de precios en una sola
    columna de precios. El DataFrame final contiene 3 columnas:
    fecha (YYYY-MM-DD), hora (HH) y precio.

    Solo se exporta un archivo el cuál tendrá la siguiente ruta:
    data_lake/cleansed/precios-horarios.csv.
    
    >>> import pandas as pd
    >>> df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    >>> df.columns
    Index(['fecha', 'hora', 'precio'], dtype='object')

    >>> df.dtypes
    fecha      object
    hora        int64
    precio    float64
    dtype: object

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import glob

    archivos = glob.glob('data_lake/raw/*csv*')

    li = []

    for archivo in archivos:
        df_temp = pd.read_csv(archivo, dtype={'Fecha': str})
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




