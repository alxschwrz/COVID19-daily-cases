# not really a webscraper
import webbrowser
import requests
import os


def download_JHU():
    # downloads up to date covid cases from John Hopkins Institute (JHU) Github.
    csv_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    # get time series of confirmed cases
    req = requests.get(csv_url)
    url_content = req.content
    if not os.path.exists('./data/'):
        os.mkdir(path='./data/')
    csv_file = open('./data/global_covid_cases.csv', 'wb')

    csv_file.write(url_content)
    csv_file.close()
