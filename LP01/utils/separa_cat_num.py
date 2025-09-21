from typing import Dict, List
import pandas as pd  # Não esqueça de importar pandas

def separa_cat_num(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Separa as colunas numéricas das categóricas.
    
    Parâmetros:
    df (pd.DataFrame): A tabela da qual serão listadas as colunas numéricas e categóricas.

    Retorna:
    Dict[str, List[str]]: Dicionário com as chaves 'categóricas' e 'numéricas' e nos valores, as listas das colunas.
    """
    colunas: Dict[str, List[str]] = {'categóricas': [], 'numéricas': []}

    tipos_categoricos: List[str] = ['object', 'category', 'string']  # Tipos de colunas categóricos
    for col in df.columns:
        if df[col].dtype in tipos_categoricos:
            colunas['categóricas'].append(col)
        else:
            colunas['numéricas'].append(col)

    return colunas
