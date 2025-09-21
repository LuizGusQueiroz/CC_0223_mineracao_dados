import pandas as pd


def get_relatorio_categoricas(df: pd.DataFrame, n: int = 5) -> str:
	"""
	Faz o relatório do DataFrame, assumindo que todas as colunas são categóricas.
	
	Parâmetros:
	df (pd.DataFrame): Tabela de onde o relatório será gerado.
	n (int): A quantidade de valores mais frequentes calculadas.

	Retorna:
	(str): O relatório gerado.
	"""

	relatorio: str = f'Top {n} valores mais frequentes das colunas categóricas.\n\n'
	# Calcula os n valores mais frequentes de cada colunas.
	for column in df.columns:
		relatorio += f'Coluna: {column}\n'
		relatorio += 'Valor   |   Contagem\n'
		# Faz a contagem da ocorrência de cada valor (Já ordenado decrescentemente).
		contagem = df[column].value_counts()
		# FIltra os top n mais frequentes.
		contagem = contagem.iloc[:n].to_dict()
		for valor in contagem:
			relatorio += f'{valor} | {contagem[valor]}\n'
		relatorio += '\n'
	
	# Calcula o índice de diversidade, que será a frequência do valor mais frequente dividido pela quantidade de valores totais.
	relatorio += '\nÍndice de diversidade\n\n'
	relatorio += 'Coluna | Índice\n'
	n_registros: int = len(df)
	for column in df.columns:
		# Cálculo da contagem do valor mais frequente.
		k: int = df[column].value_counts().max()
		relatorio += f'{column} | {round(k/n_registros, 2)}'
	

	return relatorio
