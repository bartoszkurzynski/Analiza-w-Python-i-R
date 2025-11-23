#Pobranie danych

import pandas as pd
import eurostat

pop_df = eurostat.get_data_df('demo_pjan')
# print(f"populacja na początku roku:{pop_df.head()}")
asy_df = eurostat.get_data_df('migr_asyappctza')
# print(f"wnioski o azyl:{asy_df.head()}")
mig_df = eurostat.get_data_df('migr_pop1ctz')
# print(f"populacja cudzoziemców:{mig_df.head()}")

# print(f"kolumny w mig_df:{mig_df.columns}")
# print(f"kolumny w pop_df:{pop_df.columns}")
# print(f"kolumny w asy_df:{asy_df.columns}")
# print(f"statystyki opisowe dla zmiennej populacja:{pop_df.describe()}")
# print(f"statystyki opisowe dla zmiennej wnioski o azyl:{asy_df.describe()}")
# print(f"statystyki opisowe dla zmiennej populacja cudzoziemców:{mig_df.describe()}")

#zmienne do zbudowania indeksu, 
# freq, age, sex, 'geo\TIME_PERIOD'

#usuwanie danych dla lat <2008 i >2024 dla zmiennej mig_df
mig_df=mig_df.drop(['1998','1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007'],axis=1)
# print(f"mig_df wybrane lata:{mig_df}")
#usuwanie danych dla lat <2008 i >2024 dla zmiennej pop_df
pop_df=pop_df.drop(['1960', '1961', '1962','1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980',
       '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
       '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
       '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007'],axis=1)
# print(f"pop_df wybrane lata:{pop_df}")

#dodawanie prefiksów
cols_to_prefix=['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
pop_df=pop_df.rename(columns={col:"pop"+col for col in cols_to_prefix})
mig_df=mig_df.rename(columns={col:"mig"+col for col in cols_to_prefix})
asy_df=asy_df.rename(columns={col:"asy"+col for col in cols_to_prefix})

#merge po kolumnach ['freq', 'age', 'sex', 'geo\TIME_PERIOD']

merged_df=pd.merge(pop_df, mig_df,on=['freq', 'age', 'sex', 'geo\TIME_PERIOD'],how='inner')
merged_df=pd.merge(merged_df, asy_df,on=['freq', 'age', 'sex', 'geo\TIME_PERIOD'],how='inner')
print(f"merged_df:{merged_df}")
print(f"kolumny w merged_df:{merged_df.columns}")
print(f"ilość kolumn i wierszy w merged_df:{merged_df.shape}")