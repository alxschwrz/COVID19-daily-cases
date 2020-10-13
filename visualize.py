import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def visualize():
    covid_data = pd.read_csv("./data/downloaded.csv")

    print(covid_data)
    # print(covid_data['Country/Region'])

    print(covid_data.iloc[130])
    covid_length = covid_data.iloc[130].size

    german_cases = covid_data.iloc[130, 4:covid_length]
    french_cases = covid_data.iloc[126, 4:covid_length]
    spanish_cases = covid_data.iloc[227, 4:covid_length]
    uk_cases = covid_data.iloc[257, 4:covid_length]

    new_german_cases = [y - x for x, y in zip(german_cases, german_cases[1:])]
    new_french_cases = [y - x for x, y in zip(french_cases, french_cases[1:])]
    new_spanish_cases = [y - x for x, y in zip(spanish_cases, spanish_cases[1:])]
    new_uk_cases = [y - x for x, y in zip(uk_cases, uk_cases[1:])]
    #
    # # plot cummulative cases
    plt.figure(1)
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

    plt.legend(handles=[c1_patch, c2_patch, c3_patch, c4_patch])
    plt.grid(True)

    plt.show()

    # plot new cases
    plt.figure(2)
    plt.plot(new_german_cases, 'C1')
    # plt.plot(new_french_cases, 'C2')
    # plt.plot(new_spanish_cases, 'C3')
    plt.plot(new_uk_cases, 'C4')

    # labels
    plt.title('COVID19 NEW Cases')
    plt.xlabel('days after outbreak')
    plt.ylabel('Amount')

    plt.xticks(np.arange(0, covid_length, step=50))

    c1_patch = mpatches.Patch(color='C1', label='german')
    c2_patch = mpatches.Patch(color='C2', label='french')
    c3_patch = mpatches.Patch(color='C3', label='spanish')
    c4_patch = mpatches.Patch(color='C4', label='uk')

    plt.legend(handles=[c1_patch, c2_patch, c3_patch, c4_patch])
    plt.grid(True)
    plt.show()
