#Pobranie danych

import pandas as pd
import eurostat

pop_df = eurostat.get_data_df('demo_pjan')
print(f"populacja na początku roku:{pop_df.head()}")
asy_df = eurostat.get_data_df('migr_asyappctza')
print(f"wnioski o azyl:{asy_df.head()}")
mig_df = eurostat.get_data_df('migr_pop1ctz')
print(f"populacja cudzoziemców:{mig_df.head()}")