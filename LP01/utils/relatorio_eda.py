from utils.get_relatorio_categoricas import get_relatorio_categoricas
from utils.get_relatorio_numericas import get_relatorio_numericas
from utils.salva_relatorio import salva_relatorio_txt, salva_relatorio_json
from utils.separa_cat_num import separa_cat_num
from typing import Dict, List
import pandas as pd


def relatorio_eda(df: pd.DataFrame, rel_path: str = 'relatorio') -> str:
    """
    Faz uma análise exploratória do dataset fornecido.

    Parâmetros:
    df (pd.DataFrame): Tabela que será analisada.
    rel_path (str): Caminho e o nome do relatório que será salvo.

    Retorna:
    str: Relatório no formato de texto.
    """

    # Separa as colunas numéricas das categóricas.
    colunas: Dict[str, List[str]] = separa_cat_num(df)
    cols_cat: List[str] = colunas['categóricas']
    cols_num: List[str] = colunas['numéricas']

    # Análise das categóricas.
    rel_str_cat, rel_dict_cat = get_relatorio_categoricas(df[cols_cat])

    # Análise das numéricas.
    rel_str_num, rel_dict_num = get_relatorio_numericas(df[cols_num])

    # Junta os relatórios.
    relatorio_str = rel_str_cat + rel_str_num
    relatorio_dict: Dict = {}
    relatorio_dict['categóricas'] = rel_dict_cat
    relatorio_dict['numéricas'] = rel_dict_num
    
    # Salva o relatório.
    salva_relatorio_txt(relatorio_str, rel_path)
    salva_relatorio_json(relatorio_dict, rel_path)

    return relatorio_str
