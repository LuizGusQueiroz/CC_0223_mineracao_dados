from typing import Dict, List, Tuple
import pandas as pd
import numpy as np


def get_relatorio_numericas(df: pd.DataFrame, tol_skew: float = 0.5, tol_kurt: float = 1) -> Tuple[str, Dict]:
    """
    Faz o relatório do DataFrame, assumindo que todas as colunas são numéricas.
	
	Parâmetros:
	df (pd.DataFrame): Tabela de onde o relatório será gerado.
    tol_skew (float): Tolerância para cálculo da assimetria.
    tol_kurt (float): Tolerância para cálculo da curtose.

    Retorna:
	(str): O relatório gerado em formato de string.
    (Dict): O relatório em formato de dicionário.
	"""
    
    relatorio: str = '\n\nCOLUNAS NUMÉRICAS\n\n'

    dados: Dict[str, Dict] = {column: {} for column in df.columns}

    for column in df.columns:
        col = df[column]
        # Cálculo das medidas de localização.
        dados[column]['min'] = col.min()
        dados[column]['max'] = col.max()
        dados[column]['media'] = col.mean()
        dados[column]['moda'] = col.mode().iloc[0]  # A moda retorna um series, então é preciso pegar seu elemento.
        dados[column]['mediana'] = col.median()
        q1 = round(col.quantile(0.25), 2)
        q2 = round(col.quantile(0.50), 2)
        q3 = round(col.quantile(0.75), 2)
        dados[column]['q1'] = q1
        dados[column]['q2'] = q2
        dados[column]['q3'] = q3
        # Cálculo das medidas de dispersão.
        dados[column]['amplitude'] = dados[column]['max'] - dados[column]['min']
        dados[column]['IQR'] = dados[column]['q3'] - dados[column]['q1']
        dados[column]['desvio padrão'] = col.std()
        dados[column]['variância'] = col.var()
        dados[column]['MAD'] = np.median(np.abs(col - np.median(col)))  # Desvio absoluto em relação à mediana. 
        # Cálculo das medidas de distribuição.
        dados[column]['assimetria'] = col.skew()
        dados[column]['curtose'] = col.kurt()
        dados[column]['assimetria Bowlei'] = (q3 + q1 - 2 * q2) / (q3 - q1)
        # Cálculo dos outliers.
        ls: float = dados[column]['q3'] + 1.5 * dados[column]['IQR']  # Limite superior.
        li: float = dados[column]['q1'] - 1.5 * dados[column]['IQR']  # Limite inferior.
        outliers: List[int | float] = df[column][(df[column] < li) | (df[column] > ls)].to_list()
        dados[column]['limite superior'] = ls
        dados[column]['limite inferior'] = li
        dados[column]['outliers'] = outliers
        dados[column]['total_outliers'] = len(outliers)
        # Cálculo de dados categóricos da forma da coluna.
        # Assimetria.
        skew: float = dados[column]['assimetria']
        if skew < -tol_skew:
            cat_skew = 'Cauda à esquerda'
        elif skew > tol_skew:
            cat_skew = 'Cauda à direita' 
        else:
            cat_skew = 'Simétrica'
        dados[column]['categoria simetria'] = cat_skew
        # Curtose.
        kurt: float = dados[column]['curtose']
        if kurt < -tol_kurt:
            cat_kurt = 'Platicúrtica'
        elif kurt > tol_kurt:
            cat_kurt = 'Leptocúrtica'
        else:
            cat_kurt = 'Mesocúrtica'
        dados[column]['categoria curtose'] = cat_kurt
        # Normalidade.
        if cat_skew == 'Simétrica' and cat_kurt == 'Mesocúrtica' and (
            abs(dados[column]['media'] - dados[column]['mediana']) <= 0.25 * dados[column]['desvio padrão']):
            est_norm = 'Distribuição aproximadamente normal'
        else:
            est_norm = 'Distribuição provavelmente não normal'
        dados[column]['estimação normalidade'] = est_norm
        # Preenchimento do relatório.
        
        relatorio += f'\n\tColuna: {column}\n'
        relatorio += f"""
                mínimo: {dados[column]['min']}
                máximo: {dados[column]['max']}
                média: {dados[column]['media']}
                moda: {dados[column]['moda']}
                mediana: {dados[column]['mediana']}
                q1: {dados[column]['q1']}
                q2: {dados[column]['q2']}
                q3: {dados[column]['q3']}
                amplitude: {dados[column]['amplitude']}
                IQR: {dados[column]['IQR']}
                desvio padrão: {dados[column]['desvio padrão']}
                variância: {dados[column]['variância']}
                MAD': {dados[column]['MAD']}
                assimetria: {dados[column]['assimetria']}
                curtose: {dados[column]['curtose']}
                assimetria de Bowlei: {dados[column]['assimetria Bowlei']}
                limite superior (outliers): {dados[column]['limite superior']}
                limite inferior (outliers): {dados[column]['limite inferior']}
                total de outliers: {dados[column]['total_outliers']}
                outliers: {dados[column]['outliers']}
                categoria da simetria: {dados[column]['categoria simetria']}
                categoria da curtose: {dados[column]['categoria curtose']}
                {dados[column]['estimação normalidade']}\n"""
                        
    return relatorio, dados

