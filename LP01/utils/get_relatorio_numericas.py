import pandas as pd


def get_relatorio_numericas(df: pd.DataFrame, casas_decimais: int = 2) -> str:
    """
    Faz o relatório do DataFrame, assumindo que todas as colunas são numéricas.
	
	Parâmetros:
	df (pd.DataFrame): Tabela de onde o relatório será gerado.
    n (int): Total de casas decimais a serem consideradas.

    Retorna:
	(str): O relatório gerado.
	"""
    
    relatorio: str = '\nCOLUNAS NUMÉRICAS\n\n'

    # Cálculo das medidas de localização.
    relatorio += 'Medidas de localização\n'
    relatorio += 'Coluna         | Min | Max | Média | Moda | q1 | q2 | q3\n'
    for column in df.columns:
        col = df[column]
        valor_min = round(col.min(), 2)
        valor_max = round(col.max(), 2)
        media = round(col.mean(), 2)
        moda = round(col.mode().iloc[0], 2)  # A moda retorna um series, então é preciso pegar seu elemento.
        q1 = round(col.quantile(0.25), 2)
        q2 = round(col.quantile(0.50), 2)
        q3 = round(col.quantile(0.75), 2)
        relatorio += f'{column:15}|{valor_min:5}|{valor_max:5}|{media:7}|{moda:6}|{q1:4}|{q2:4}|{q3:4}\n'

    return relatorio
