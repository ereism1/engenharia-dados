import pandas as pd

df = pd.read_parquet(
    "data/raw/clientes.parquet"
)

print(df.head())
