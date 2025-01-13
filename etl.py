# Carregando bibliotecas
import pandas as pd
import os 
import glob
from log import log_decorator

# Criando uma função para ler e consolidar os json

@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Função que transforma
@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total de vendas"] = df['Quantidade'] * df['Venda']
    return df

# Função que da load em CSV ou Parquet

@log_decorator
def carregar_dados(df: pd.DataFrame, formato_de_saida: list):
    """
    parametro que vai ser ou CSV ou PARQUET ou OS DOIS
    """
    for formato in formato_de_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = (extrair_dados(pasta))
    data_frame_calculado = (calcular_kpi_de_total_de_vendas(data_frame))
    carregar_dados(data_frame_calculado,formato_de_saida)
