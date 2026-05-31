import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL")
)

tabelas = [
    "clientes",
    "produtos",
    "formas_pagamento",
    "vendas_novo"
]

for tabela in tabelas:

    print(f"Extraindo {tabela}...")

    df = pd.read_sql(
        f"SELECT * FROM {tabela}",
        engine
    )

    df.to_parquet(
        f"data/raw/{tabela}.parquet",
        index=False
    )

    print(f"{tabela} salva!")