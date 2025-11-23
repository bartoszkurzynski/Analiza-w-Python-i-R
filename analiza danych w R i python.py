#Pobranie danych

import pandas as pd
import eurostat

pop_df = eurostat.get_data_df('demo_pjan')
# print(f"populacja na początku roku:{pop_df.head()}")
asy_df = eurostat.get_data_df('migr_asyappctza')
# print(f"wnioski o azyl:{asy_df.head()}")
mig_df = eurostat.get_data_df('migr_pop1ctz')
# print(f"populacja cudzoziemców:{mig_df.head()}")



# Wspólna lista lat, które nas interesują
years = [str(y) for y in range(2008, 2025)]

# Usuwanie zbędnych kolumn
cols_drop = ['unit', 'age', 'freq']

pop_df = pop_df.drop(columns=cols_drop, errors='ignore')
mig_df = mig_df.drop(columns=cols_drop, errors='ignore')
asy_df = asy_df.drop(columns=cols_drop + ['citizen', 'applicant'], errors='ignore')

# Usuwanie UNK z asy_df
asy_df = asy_df[asy_df['sex'] != "UNK"]

# --------------------------
# 3. Konwersja do long-format
# --------------------------

# Upewniamy się, że kolumna z krajem/regionem nazywa się tak samo
geo_col = 'geo\\TIME_PERIOD' if 'geo\\TIME_PERIOD' in pop_df.columns else 'geo'

# POP long
pop_long = pop_df.melt(
    id_vars=['sex', geo_col],
    value_vars=years,
    var_name='year',
    value_name='pop'
)

# MIG long
mig_long = mig_df.melt(
    id_vars=['sex', geo_col],
    value_vars=years,
    var_name='year',
    value_name='mig'
)

# ASY long
asy_long = asy_df.melt(
    id_vars=['sex', geo_col],
    value_vars=years,
    var_name='year',
    value_name='asy'
)

# --------------------------
# 4. Podgląd wyników
# --------------------------
print("pop_long:")
print(pop_long.head())

print("\nmig_long:")
print(mig_long.head())

print("\nasy_long:")
print(asy_long.head())


# print(f"kolumny w mig_df:{mig_df.columns}")
# print(f"kolumny w pop_df:{pop_df.columns}")
# print(f"kolumny w asy_df:{asy_df.columns}")
# print(f"kolumny w mig_df:{mig_df['unit']}")
# print(f"kolumny w pop_df:{pop_df['unit']}")
# print(f"kolumny w asy_df:{asy_df['unit']}")
# print(f"kolumny w mig_df:{mig_df['freq']}")
# print(f"kolumny w pop_df:{pop_df['freq']}")
# print(f"kolumny w asy_df:{asy_df['freq']}")
# print(f"kolumny w mig_df:{mig_df['sex']}")
# print(f"kolumny w pop_df:{pop_df['sex']}")
# print(f"kolumny w asy_df:{asy_df['sex']}")
# print(f"kolumny w mig_df:{mig_df['age']}")
# print(f"kolumny w pop_df:{pop_df['age']}")
# print(f"kolumny w asy_df:{asy_df['age']}")
# print(f"kolumny w mig_df:{mig_df['geo\TIME_PERIOD']}")
# print(f"kolumny w pop_df:{pop_df['geo\TIME_PERIOD']}")
# print(f"kolumny w asy_df:{asy_df['geo\TIME_PERIOD']}")

# print(f"wartości unikalne w mig_df['freq']:{mig_df['freq'].unique()}")
# print(f"wartości unikalne w pop_df['freq']:{pop_df['freq'].unique()}")
# print(f"wartości unikalne w asy_df['freq']:{asy_df['freq'].unique()}")
# print(f"wartości unikalne w mig_df['sex']:{mig_df['sex'].unique()}")
# print(f"wartości unikalne w pop_df['sex']:{pop_df['sex'].unique()}")
# print(f"wartości unikalne w asy_df['sex']:{asy_df['sex'].unique()}")
# print(f"wartości unikalne w mig_df['age']:{mig_df['age'].unique()}")
# print(f"wartości unikalne w pop_df['age']:{pop_df['age'].unique()}")
# print(f"wartości unikalne w asy_df['age']:{asy_df['age'].unique()}")
# print(f"wartości unikalne w mig_df['geo\TIME_PERIOD']:{mig_df['geo\TIME_PERIOD'].unique()}")
# print(f"wartości unikalne w pop_df['geo\TIME_PERIOD']:{pop_df['geo\TIME_PERIOD'].unique()}")
# print(f"wartości unikalne w asy_df['geo\TIME_PERIOD']:{asy_df['geo\TIME_PERIOD'].unique()}")


# print(f"statystyki opisowe dla zmiennej populacja:{pop_df.describe()}")
# print(f"statystyki opisowe dla zmiennej wnioski o azyl:{asy_df.describe()}")
# print(f"statystyki opisowe dla zmiennej populacja cudzoziemców:{mig_df.describe()}")

#zmienne do zbudowania indeksu, 
# freq, age, sex, 'geo\TIME_PERIOD'

# #usuwanie danych dla lat <2008 i >2024 dla zmiennej mig_df oraz kolumny 'unit'
# asy_df=asy_df.drop(['unit','age','freq','citizen', 'applicant'],axis=1)
# asy_df = asy_df[asy_df['sex'] != "UNK"]
# # asy_df=asy_df.drop(asy_df[asy_df['sex']=="UNK"].index,axis=0,inplace=True)
# mig_df=mig_df.drop(['unit','age','freq','1998','1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007'],axis=1)
# # print(f"mig_df wybrane lata:{mig_df}")
# #usuwanie danych dla lat <2008 i >2024 dla zmiennej pop_df
# pop_df=pop_df.drop(['unit','age','freq','1960', '1961', '1962','1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
#        '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980',
#        '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
#        '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
#        '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007'],axis=1)
# # print(f"pop_df wybrane lata:{pop_df}")

# print(f"kolumny w mig_df:{mig_df.columns}")
# print(f"kolumny w pop_df:{pop_df.columns}")
# print(f"kolumny w asy_df:{asy_df.columns}")


# #dodawanie prefiksów
# cols_to_prefix=['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
# pop_df=pop_df.rename(columns={col:"pop"+col for col in cols_to_prefix})
# mig_df=mig_df.rename(columns={col:"mig"+col for col in cols_to_prefix})
# asy_df=asy_df.rename(columns={col:"asy"+col for col in cols_to_prefix})

# pop_long = pop_df.melt(
#     id_vars=['sex', 'geo\\TIME_PERIOD'],
#     value_vars=cols_to_prefix,
#     var_name='year',
#     value_name='pop'
# )

# print(f"pop_long:{pop_long}")
# #merge po kolumnach [ 'sex', 'geo\TIME_PERIOD']

# # merged_df=pd.merge(pop_df, mig_df,on=['sex', 'geo\TIME_PERIOD'],how='inner')
# # merged_df=pd.merge(merged_df, asy_df,on=['sex', 'geo\TIME_PERIOD'],how='inner')
# # print(f"merged_df:{merged_df}")
# # print(f"kolumny w merged_df:{merged_df.columns}")
# # print(f"ilość kolumn i wierszy w merged_df:{merged_df.shape}")
merged_df = (
    pop_long
    .merge(mig_long, on=['sex', geo_col, 'year'], how='inner')
    .merge(asy_long, on=['sex', geo_col, 'year'], how='inner')
)

print("\n=== MERGED DATAFRAME ===")
print(merged_df.head())
print(f"\nRozmiar merged_df: {merged_df.shape}")
print(f"\nKolumny: {merged_df.columns.tolist()}")