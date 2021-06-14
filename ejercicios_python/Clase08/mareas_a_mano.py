import pandas as pd


df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

dh = df['12-25-2014':].copy()
delta_t = -1
delta_h = 25.5
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
