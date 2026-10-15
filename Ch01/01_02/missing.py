# %%
import pandas as pd

# %%
df = pd.read_csv('C:/Users/Jabulani.Mcineka/workspace/data-cleaning-in-python-essential-training-3086536/Ch01/01_02/cart.csv', parse_dates=['date'])
df 

# %%
df['amount'].astype('Int32')

# %%
df.isnull()

# %%
df.isnull().any(axis=1)
