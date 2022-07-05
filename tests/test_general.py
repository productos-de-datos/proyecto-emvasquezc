from src.data import *
from src.features import *
from src.models import *
from src.visualization import *



def test_ingest_data():
    ingest_data()
    import os
    assert os.path.isfile("data_lake/landing/1995.xlsx")

def test_transform_data():
    transform_data()
    import os
    assert os.path.isfile("data_lake/raw/1995.csv")

def test_clean_data():
    clean_data()
    import pandas as pd
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')        
    assert str(df.columns) == "Index(['fecha', 'hora', 'precio'], dtype='object')"


def test_compute_daily_prices():
    compute_daily_prices()
    import pandas as pd
    df = pd.read_csv('data_lake/business/precios-diarios.csv', \
    parse_dates=['fecha'], index_col=['fecha'])
    assert pd.infer_freq(df.index) == 'D'


def test_compute_monthly_prices():
    compute_monthly_prices()
    import pandas as pd
    df = pd.read_csv('data_lake/business/precios-mensuales.csv', \
    parse_dates=['fecha'], index_col=['fecha'])
    assert pd.infer_freq(df.index) == 'MS'

def test_pipeline():
    pass

def test_make_daily_prices_plot():
    make_daily_prices_plot()
    import os
    assert os.path.isfile('data_lake/business/reports/figures/daily_prices.png')

def test_make_monthly_prices_plot():
    make_monthly_prices_plot()
    assert os.path.isfile('data_lake/business/reports/figures/monthly_prices.png')

def test_make_features():
    make_features()
    import pandas as pd
    df = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    assert (str(df.columns) ==
    "Index(['fecha', 'precios_dias_anteriores', 'precio_escalado'], dtype='object')")

def test_train_daily_model():
    train_daily_model()
    import os
    assert os.path.isfile('src/models/precios-diarios.pkl')


def test_make_forecasts():
    make_forecasts()
    import pandas as pd
    df = pd.read_csv('data_lake/business/forecasts/precios-diarios.csv')
    assert (str(df.columns) ==
    "Index(['fecha', 'precio_real', 'pronostico'], dtype='object')")