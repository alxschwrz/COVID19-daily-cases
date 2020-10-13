import webbrowser
import requests


def download():
    #base_url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series'
    #webbrowser.open(base_url)

    csv_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    req = requests.get(csv_url)
    url_content = req.content
    csv_file = open('./data/downloaded.csv', 'wb')

    csv_file.write(url_content)
    csv_file.close()
