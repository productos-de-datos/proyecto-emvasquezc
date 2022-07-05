def transform_data():
    """
    Esta función convierte todos los archivos xlsx y xls a csv.
    Los archivos tienen las columnas: fecha (YYYY-MM-DD), horas
    (HH). Los archivos son guardados en la capa raw.

    >>> transform_data()
    >>> import os
    >>> os.path.isfile("data_lake/raw/1995.csv")
    True

    >>> os.path.isfile("data_lake/raw/2021.csv")
    True

    """
    # raise NotImplementedError("Implementar esta función")

    import glob
    import pandas as pd

    archivos = glob.glob("data_lake/landing/*xls*")
    usecols = ["Fecha"] + [str(i) for i in range(24)]
    dtype = {"Fecha": str}

    for archivo in archivos:
        df = pd.read_excel(archivo, dtype=dtype)
        # Eliminar las filas que no tienen datos
        if df.columns[0] != "Fecha":
            indice_inicio_df = int(df[df.iloc[:, 0] == "Fecha"].index.values) + 1
            df = pd.read_excel(
                archivo, usecols=usecols, skiprows=indice_inicio_df, dtype=dtype
            )
        # Quitar 00:00:00 de las fechas
        df["Fecha"] = df["Fecha"].astype(str).apply(lambda x: x.split(" ")[0])
        name_file = archivo.rsplit("/")[-1]
        df.to_csv("data_lake/raw/" + name_file.split(".")[0] + ".csv", index=False)


def test_transform_data():
    import os

    assert os.path.isfile("data_lake/raw/1995.csv") is True


if __name__ == "__main__":

    transform_data()
    import doctest

    doctest.testmod()
