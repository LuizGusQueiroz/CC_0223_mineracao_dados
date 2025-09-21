import os


def init_dir(dir_name: str) -> None:
	"""
	Verifica se um diretório já existe, caso não existe, cria ele.
	
	Parâmetros:
	dir_name (str): Nome do diretório que será criado.
	"""
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)

