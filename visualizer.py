import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme()
import matplotlib.patches as mpatches
from Countrydetails import country as countdet


def visualize(country="Germany"):
    country = country
    covid_df = pd.read_csv("./data/global_covid_cases.csv")
    days_since_outbreak = len(covid_df.columns[4:])
    # dates = covid_df.columns[4:].to_list()
    cumm_country_cases = covid_df[covid_df['Country/Region'] == country].iloc[0, 5:days_since_outbreak]

    new_cases_df = covid_df.copy()
    for i in range(4, days_since_outbreak):
        new_cases_df.iloc[:, i + 1] = covid_df.iloc[:, i + 1] - covid_df.iloc[:, i]
    new_country_cases = new_cases_df[new_cases_df['Country/Region'] == country].iloc[0, 5:days_since_outbreak]

    # drop cols with no population information available in current package
    drop_arr = []
    for idc, curr_country in enumerate(covid_df['Country/Region']):
        if not isinstance(countdet.country_details(curr_country).population(), int):
            drop_arr.append(idc)
    covid_df = covid_df.drop(drop_arr)

    covid_df['Population'] = covid_df['Country/Region']
    covid_df['Population'] = covid_df['Population'].apply(lambda x: countdet.country_details(x).population())
    col_names = covid_df.columns.insert(4, "Population")[:-1]
    covid_df = covid_df.reindex(columns=col_names)

    incidence_df = covid_df.copy()
    for i in range(5, days_since_outbreak - 2):
        incidence_df.iloc[:, i + 7] = (covid_df.iloc[:, i + 7] - covid_df.iloc[:, i]) / covid_df['Population'] * 100000
    incidence = incidence_df[incidence_df['Country/Region'] == country].iloc[0, 5:days_since_outbreak]

    fig, axs = plt.subplots(3, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1, 1]})
    fig.suptitle('Covid Cases {}'.format(country))

    axs[0].plot(incidence)
    axs[0].set_title('7-day incidence')
    axs[0].set_ylabel('cases in 7 days / 100.000')
    axs[0].set_xticks(np.arange(0, days_since_outbreak, step=100))
    axs[0].grid(True)

    axs[1].plot(new_country_cases)
    axs[1].set_title('new cases [total]')
    axs[1].set_ylabel('new cases')
    axs[1].set_xticks(np.arange(0, days_since_outbreak, step=100))
    axs[1].grid(True)

    axs[2].plot(cumm_country_cases)
    axs[2].set_title('cummulative cases [total]')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('Total cases')
    axs[2].set_xticks(np.arange(0, days_since_outbreak, step=100))
    axs[2].grid(True)
    plt.show()
    # c1_patch = mpatches.Patch(color='C1', label=country)
    # plt.legend(handles=[c1_patch])
