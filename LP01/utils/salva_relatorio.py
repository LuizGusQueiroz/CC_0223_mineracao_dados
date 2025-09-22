from typing import Dict
import json


def salva_relatorio_txt(relatorio: str, rel_path: str='relatorio_eda') -> None:
    file_name = f'{rel_path}.txt'
    with open(file_name, 'w') as file:
        file.write(relatorio)


def salva_relatorio_json(relatorio: Dict, rel_path: str='relatorio_eda') -> None:
    file_name = f'{rel_path}.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(relatorio, file, indent=4, ensure_ascii=False, default=str)
