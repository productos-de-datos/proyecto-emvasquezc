def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    # raise NotImplementedError("Implementar esta función")

    import glob
    import pandas as pd
    archivos = glob.glob('data_lake/landing/*xls*')
    usecols = ['Fecha'] + [str(i) for i in range(24)]
    dtype = {'Fecha': str}
    
    for archivo in archivos:
        print(archivo)
        df = pd.read_excel(archivo, dtype=dtype)
        # Eliminar las filas que no tienen datos
        if df.columns[0] != 'Fecha':
            indice_inicio_df = int(df[df.iloc[:, 0] == 'Fecha'].index.values) + 1
            df = pd.read_excel(archivo, usecols=usecols, 
                                skiprows=indice_inicio_df, dtype=dtype)
        # Quitar 00:00:00 de las fechas
        df['Fecha'] = df['Fecha'].astype(str).apply(lambda x: x.split(' ')[0])
        name_file = archivo.rsplit('/')[-1]
        df.to_csv('data_lake/raw/' + name_file.split('.')[0] + '.csv', index=False)   



if __name__ == "__main__":
    transform_data()
    import doctest

    doctest.testmod()
