import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def visualize():
    country = "China"
    covid_df = pd.read_csv("./data/downloaded.csv")
    days_since_outbreak = len(covid_df.columns[4:])
    dates = covid_df.columns[4:].to_list()
    country_cases = covid_df[covid_df['Country/Region'] == country].iloc[0, 4:days_since_outbreak]

    new_cases_df = covid_df.copy()

    for i in range(4, days_since_outbreak):
        new_cases_df.iloc[:, i + 1] = covid_df.iloc[:, i + 1] - covid_df.iloc[:, i]
    new_country_cases = new_cases_df[new_cases_df['Country/Region'] == country].iloc[0, 4:days_since_outbreak]
    #new_country_cases = [y - x for x, y in zip(country_cases, country_cases[1:])]

    #plt.plot(covid_df.columns[4:], new_country_cases)
    plt.plot(new_country_cases)
    #plt.legend("Germany{}".format(country))
    plt.title('COVID19 NEW Cases')
    plt.xlabel('Date')
    plt.ylabel('Total cases')
    #plt.grid(True)
    plt.xticks(np.arange(0, days_since_outbreak, step=100))
    plt.show()


def visualizer():
    # this function plots covid19 data
    covid_data = pd.read_csv("./data/downloaded.csv")
    covid_deaths = pd.read_csv("./data/downloaded_deaths.csv")

    # print(covid_data)
    # print(covid_data['Country/Region'])

    # print(covid_data.iloc[130])
    covid_length = covid_data.iloc[130].size

    german_cases = covid_data.iloc[130, 4:covid_length]
    french_cases = covid_data.iloc[126, 4:covid_length]
    spanish_cases = covid_data.iloc[227, 4:covid_length]
    uk_cases = covid_data.iloc[257, 4:covid_length]
    sweden_cases = covid_data.iloc[231, 4:covid_length]

    new_german_cases = [y - x for x, y in zip(german_cases, german_cases[1:])]
    new_french_cases = [y - x for x, y in zip(french_cases, french_cases[1:])]
    new_spanish_cases = [y - x for x, y in zip(spanish_cases, spanish_cases[1:])]
    new_uk_cases = [y - x for x, y in zip(uk_cases, uk_cases[1:])]
    new_sweden_cases = [y - x for x, y in zip(sweden_cases, sweden_cases[1:])]
    #

    # # plot cummulative cases
    plt.figure(1)
    # with plt.style.context('dark_background'):
    plt.plot(german_cases, 'C1')
    plt.plot(french_cases, 'C2')
    plt.plot(spanish_cases, 'C3')
    plt.plot(uk_cases, 'C4')

    # labels
    plt.title('Cummulative COVID19 Cases')
    plt.xlabel('date')
    plt.ylabel('Amount')

    plt.xticks(np.arange(0, covid_length, step=50))

    c1_patch = mpatches.Patch(color='C1', label='german')
    c2_patch = mpatches.Patch(color='C2', label='french')
    c3_patch = mpatches.Patch(color='C3', label='spanish')
    c4_patch = mpatches.Patch(color='C4', label='uk')
    c5_patch = mpatches.Patch(color='C5', label='sweden')

    plt.legend(handles=[c1_patch, c2_patch, c3_patch, c4_patch, c5_patch])
    plt.grid(True)

    plt.show()

    # plot new cases
    plt.figure(2)
    plt.plot(new_german_cases, 'C1')
    # plt.plot(new_french_cases, 'C2')
    # plt.plot(new_spanish_cases, 'C3')
    # plt.plot(new_uk_cases, 'C4')
    # plt.plot(new_sweden_cases, 'C5')

    # labels
    plt.title('COVID19 NEW Cases')
    plt.xlabel('days after outbreak')
    plt.ylabel('Amount')

    plt.xticks(np.arange(0, covid_length, step=50))

    plt.legend(handles=[c1_patch, c2_patch, c3_patch, c4_patch, c5_patch])
    plt.grid(True)
    plt.show()

    print('new infections germany: ', new_german_cases[-1])

    # # 7 day incidence

    # # death rate
    german_deaths = covid_deaths.iloc[130, 4:covid_length]
    swedish_deaths = covid_deaths.iloc[231, 4:covid_length]
    french_deaths = covid_deaths.iloc[126, 4:covid_length]

    new_german_deaths = [y - x for x, y in zip(german_deaths, german_deaths[1:])]
    new_swedish_deaths = [y - x for x, y in zip(swedish_deaths, swedish_deaths[1:])]
    new_french_deaths = [y - x for x, y in zip(french_deaths, french_deaths[1:])]

    plt.figure(3)
    plt.plot(german_deaths, 'C1')
    plt.plot(french_deaths, 'C2')
    plt.plot(swedish_deaths, 'C5')

    # labels
    plt.title('Cummulative COVID19 Deaths')
    plt.xlabel('date')
    plt.ylabel('Amount')

    plt.xticks(np.arange(0, covid_length, step=50))

    plt.legend(handles=[c1_patch, c2_patch, c5_patch])
    plt.grid(True)

    plt.show()

    plt.figure(4)
    plt.plot(new_german_deaths, 'C1')
    # plt.plot(new_french_deaths, 'C2')
    # plt.plot(new_swedish_deaths, 'C5')

    plt.title('Daily COVID19 Deaths')
    plt.xlabel('date')
    plt.ylabel('Amount')

    plt.xticks(np.arange(0, covid_length, step=50))

    plt.legend(handles=[c1_patch, c2_patch, c5_patch])
    plt.grid(True)

    plt.show()
