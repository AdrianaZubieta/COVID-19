import pandas
import statistics as st
daily_report = pandas.read_csv('csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv')
 
for index, row in daily_report.iterrows():
    print("{} country: {} - Deaths {}".format(index, row['Country/Region'], row['Deaths']))


