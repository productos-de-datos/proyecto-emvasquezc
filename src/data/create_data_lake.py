def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    # raise NotImplementedError("Implementar esta función")

    import os

    paths = ['data_lake', 'data_lake/landing', 'data_lake/raw', 'data_lake/cleansed', 
    'data_lake/business', 'data_lake/business/reports', 'data_lake/business/reports/figures',
    'data_lake/business/features', 'data_lake/business/forecasts']

    for i in paths:
        if not os.path.exists(i):
            os.makedirs(i)


if __name__ == "__main__":
    create_data_lake()
    import doctest

    doctest.testmod()
