import glob as g
import pandas as pd
import numpy as np

# file = pd.read_csv('csse_covid_19_data/csse_covid_19_daily_reports/01-22-2020.csv')

files = g.glob('csse_covid_19_data/csse_covid_19_daily_reports/*.csv')

csvs = [pd.read_csv(fu) for fu in files] 

dataframe = pd.concat(csvs, ignore_index=True)
dataframe.to_csv('covid.csv')


