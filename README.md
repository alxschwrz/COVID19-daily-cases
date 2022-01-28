# COVID19-daily-cases

Super simple script, which downloads and plots recent COVID-19 cases from the JHU repository.
New cases and 7-Day incidence are computed and displayed. User can select a country and plot up-to-date 
curves.


## Installation


```bash
git clone https://github.com/alxschwrz/COVID19-daily-cases.git
cd COVID19-daily-cases
pip3 install -r requirements.txt
```

## Example
Executing the `main.py` and passing the respective name of the country will generate a plot of the countries respective covid cases. Default country is set to Germany.
```bash
python3 main.py Netherlands
```
