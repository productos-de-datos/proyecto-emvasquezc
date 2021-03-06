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
from luigi import Task


class luigi_ingest_data(Task):
    def output(self):
        return luigi.LocalTarget("data_lake/landing/result.txt")

    def run(self):
        from ingest_data import ingest_data

        with self.output().open("w") as files_ingested:
            ingest_data()


class luigi_transform_data(Task):
    def requires(self):
        return luigi_ingest_data()

    def output(self):
        return luigi.LocalTarget("data_lake/raw/result.txt")

    def run(self):
        from transform_data import transform_data

        with self.output().open("w") as files_transformed:
            transform_data()


class luigi_clean_data(Task):
    def requires(self):
        return luigi_transform_data()

    def output(self):
        return luigi.LocalTarget("data_lake/cleansed/result.txt")

    def run(self):
        from clean_data import clean_data

        with self.output().open("w") as f:
            clean_data()


class luigi_compute_daily_prices(Task):
    def requires(self):
        return luigi_clean_data()

    def output(self):
        return luigi.LocalTarget("data_lake/business/result.txt")

    def run(self):
        from compute_daily_prices import compute_daily_prices

        with self.output().open("w") as f:
            compute_daily_prices()


class luigi_compute_monthly_prices(Task):
    def requires(self):
        return luigi_compute_daily_prices()

    def output(self):
        return luigi.LocalTarget("data_lake/business/result.txt")

    def run(self):
        from compute_monthly_prices import compute_monthly_prices

        with self.output().open("w") as f:
            compute_monthly_prices()


if __name__ == "__main__":

    luigi.run(["luigi_compute_monthly_prices", "--local-scheduler"])

    # raise NotImplementedError("Implementar esta funci??n")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
