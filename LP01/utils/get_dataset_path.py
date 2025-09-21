from tkinter import filedialog
import tkinter as tk


def get_dataset_path() -> str:
	"""
	Abre uma janela para que o usuário escolha o caminho do dataset.
	
	Retorna:
	str: O caminho para o dataset.
	"""
	# Inicializa a janela principal.
	root = tk.Tk()
	root.withdraw()
	# Abre a janela para escolher o dataset.
	dataset_path = filedialog.askopenfilename(title='Escolha o seu dataset')
	return dataset_path

