def salva_relatorio(relatorio: str, nome: str = 'relatorio_eda') -> None:
    file_name = f'{nome}.txt'
    with open(file_name, 'w') as file:
        file.write(relatorio)

