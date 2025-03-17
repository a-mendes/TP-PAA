import os
from consts import EXPERIMENT_1_DIR, EXPERIMENT_2_DIR

def read_instance(experiment, instance):
    if experiment not in [1, 2] or not (1 <= instance <= 20):
        raise ValueError("Experimento deve ser 1 ou 2 e instance deve estar entre 1 e 20")

    base_path = EXPERIMENT_1_DIR if experiment == 1 else EXPERIMENT_2_DIR
    file_path = os.path.join(base_path, f'{instance}.txt')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    backpack_weight = int(lines[0].strip())
    itens = []

    for line in lines[1:]:
        weight, value = map(int, line.strip().split())
        itens.append([weight, value])

    return backpack_weight, itens