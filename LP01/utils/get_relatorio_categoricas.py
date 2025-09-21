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
    relatorio: str = '\nCOLUNAS CATEGÓRICAS\n\n'
    n_registros: int = len(df)  # Quantidade de registros.

    for column in df.columns:
        col = df[column]

        # Contagem de valores
        contagem = col.value_counts()
        contagem_top_n = contagem.iloc[:n].to_dict()

        # Índice de diversidade
        k: int = contagem.max()  # frequência da moda
        indice: float = round(100 * k / n_registros, 2)

        # Preenchimento do relatório
        relatorio += f'\tColuna: {column}\n'
        relatorio += f'\t\tTop {n} valores mais frequentes:\n'
        for valor in contagem_top_n:
            relatorio += f'\t\t{valor} | {contagem[valor]}\n'
        relatorio += f'\tÍndice de diversidade: {indice}%\n\n'

    return relatorio
