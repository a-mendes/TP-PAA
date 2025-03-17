import os
from consts import EXPERIMENT_1_DIR, EXPERIMENT_2_DIR

def ler_dados(experimento, instancia):
    if experimento not in [1, 2] or not (1 <= instancia <= 20):
        raise ValueError("Experimento deve ser 1 ou 2 e instancia deve estar entre 1 e 20")

    base_path = EXPERIMENT_1_DIR if experimento == 1 else EXPERIMENT_2_DIR
    file_path = os.path.join(base_path, f'instancia{instancia}.txt')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    peso_mochila = int(lines[0].strip())
    matriz_itens = []

    for line in lines[1:]:
        peso, valor = map(int, line.strip().split())
        matriz_itens.append([peso, valor])

    return peso_mochila, matriz_itens