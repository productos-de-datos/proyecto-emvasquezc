"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """
    Este modulo descarga todos los archivos del histórico de
    los precios de la energía, que se encuentra en el repositorio
    jdvelasq/datalabs/precio_bolsa_nacional/xls/.

    Los archivos son guardados en la capa landing del data_lake.

    >>> import os
    >>> os.path.isfile("data_lake/landing/1995.xlsx")
    True

    >>> os.path.isfile("data_lake/landing/2021.xlsx")
    True

    """
    # raise NotImplementedError("Implementar esta función")

    import requests
    import os

    for i in range(1995, 2022):
        if i in range(2016, 2018):
            wdir = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true".format(
                i
            )
            with open("data_lake/landing/" + str(i) + ".xls", "wb") as f:
                f.write(requests.get(wdir).content)
        else:
            wdir = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true".format(
                i
            )
            with open("data_lake/landing/" + str(i) + ".xlsx", "wb") as f:
                f.write(requests.get(wdir).content)

    # pip install PyGithub
    # import github
    # import requests
    # g = github.Github()
    # repo = g.get_repo('jdvelasq/datalabs')
    # contents = repo.get_contents('datasets/precio_bolsa_nacional/xls')

    # for contentFile in contents:
    #     download_url = contentFile.download_url
    #     nombre_archivo = download_url.rsplit('/', 1)[1]
    #     with open('data_lake/landing/' + nombre_archivo, 'wb') as f:
    #         f.write(requests.get(download_url).content)


if __name__ == "__main__":
    ingest_data()
    import doctest

    doctest.testmod()
