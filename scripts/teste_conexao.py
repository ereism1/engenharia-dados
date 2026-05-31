import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL")
    
)

df = pd.read_sql(
    "SELECT * FROM clientes",
    engine
)

df.to_parquet(
    "data/raw/clientes.parquet",
    index=False
)

print("Arquivo salvo com sucesso!")     