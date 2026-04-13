import pandas as pd
import numpy as np
import json
import scipy
import re

# funkcja pomocnicza obsługuje np. 'D' jako '1D'
def get_td(freq_str):
    if freq_str and not freq_str[0].isdigit():
        freq_str = '1' + freq_str
    return pd.to_timedelta(freq_str)




# ex 0 
with open("lab5_params.json", "r", encoding="utf-8") as plik:
    dane = json.load(plik)




# ex 1
df = pd.read_csv("lab5_timeseries.csv")

df.columns = (
    df.columns
      .str.lower()
      .str.replace(r'[^a-z]', "_", regex=True)
)

# konwersja daty i ustawienie indeksu
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], format="mixed")
df = df.set_index(df.columns[0])

# ustawienie oryginalnej częstotliwości
original_frequency = dane["original_frequency"]
df = df.asfreq(original_frequency)



# zachowujemy kopię danych z zadania 1 
df_orig = df.copy()
df.to_pickle("lab5_ex01_timeseries.pkl")




# ex 2
target_frequency = dane["target_frequency"]
df_ex02 = df_orig.asfreq(target_frequency)
df_ex02.to_pickle("lab5_ex02_freq.pkl")





# ex 3
periods = dane["downsample_periods"]
units = dane["downsample_units"]
rule_down = f"{periods}{units.upper()}"

# obliczamy ile oryginalnych próbek powinno być w nowym oknie
td_rule_down = get_td(rule_down)
td_orig = get_td(original_frequency)
expected_samples = int(td_rule_down / td_orig)


df_downsampled = df_orig.resample(rule_down).sum(min_count=expected_samples)
df_downsampled.to_pickle("lab5_ex03_downsampled.pkl")






# ex 4
upsample_periods = dane["upsample_periods"]
upsample_units = dane["upsample_units"]
rule_up = f"{upsample_periods}{upsample_units.upper()}"

interpolation = dane["interpolation"]
interpolation_order = dane["interpolation_order"]

# upsampling z interpolacją
df_upsampled = df_orig.resample(rule_up).interpolate(method=interpolation, order=interpolation_order)

# skalowanie wartości (ratio = nowa_częstotliwość / stara_częstotliwość)
td_rule_up = get_td(rule_up)
ratio = td_rule_up / td_orig
df_scaled = df_upsampled * ratio

df_scaled.to_pickle("lab5_ex04_upsampled.pkl")





# ex 5
df_sensors = pd.read_pickle("lab5_sensors.pkl")
sensors_periods = dane["sensors_periods"]
sensors_units = dane["sensors_units"]
rule_sensors = f"{sensors_periods}{sensors_units.upper()}"  

# do formatu szerokiego
df_wide = df_sensors.pivot(columns='device_id', values='value')

#wyznaczenie nowej siatki czasu 
start = df_wide.index.min().floor(rule_sensors)  
end = df_wide.index.max().floor(rule_sensors)   
new_index = pd.date_range(start=start, end=end, freq=rule_sensors)

# połączenie starego indeksu z nowym
combined_index = df_wide.index.union(new_index)
df_aligned = df_wide.reindex(combined_index)

#interpolacja liniowa 
df_aligned = df_aligned.interpolate(method='linear')

# wybranie tylko punktów z nowej siatki czasu
df_aligned = df_aligned.loc[new_index]

# usunięcie wierszy, gdzie nie dało się interpolować 
df_aligned = df_aligned.dropna(how='any')

# przywrócenie nazwy indeksu kolumn 
df_aligned.columns.name = 'device_id'

df_aligned.to_pickle("lab5_ex05_sensors.pkl")