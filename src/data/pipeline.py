"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""

import luigi

class luigi_ingest_data:

    def output(self):
        return luigi.LocalTarget('data_lake/landing/result.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as files_ingested:
            ingest_data()

class luigi_transform_data:

    def requires(self):
        return luigi_ingest_data()

    def output(self):
        return luigi.LocalTarget('data_lake/raw/results2.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as files_transformed:
            transform_data()

class luigi_clean_data:

    def requires(self):
        return luigi_transform_data()

    def output(self):
        return luigi.LocalTarget('data_lake/cleansed/results3.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as f:
            clean_data()

class luigi_compute_daily_prices:

    def requires(self):
        return luigi_clean_data()

    def output(self):
        return luigi.LocalTarget('data_lake/business/results4.csv')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as f:
            compute_daily_prices()

class luigi_compute_monthly_prices:

    def requires(self):
        return luigi_compute_daily_prices()

    def output(self):
        return luigi.LocalTarget('data_lake/business/results5.csv')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as f:
            compute_monthly_prices()


if __name__ == "__main__":

    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
