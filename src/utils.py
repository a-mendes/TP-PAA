import os
from consts import EXPERIMENT_1_DIR, EXPERIMENT_2_DIR, LOG_DIR
import consts as c

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

def save_logs(experiment, instance, algorithm, log_type, log, write_mode='a'):
    if experiment not in [1, 2] or not (1 <= instance <= 20):
        raise ValueError("Experimento deve ser 1 ou 2 e instance deve estar entre 1 e 20")

    base_path = os.path.join(EXPERIMENT_1_DIR if experiment == 1 else EXPERIMENT_2_DIR, LOG_DIR, algorithm)
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    file_path = os.path.join(base_path, f'{algorithm}_{log_type}_logs.txt')
    with open(file_path, write_mode) as file:
        if isinstance(log, tuple):
            file.write('\t'.join(map(str, log)) + '\n')
        else:
            file.write(f'{log}\n')

def last_instance_executed(experiment, algorithm):
    base_path = os.path.join(EXPERIMENT_1_DIR if experiment == 1 else EXPERIMENT_2_DIR, LOG_DIR, algorithm)
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    file_path = os.path.join(base_path, f'{algorithm}_{c.LAST_INSTANCE_EXECUTED}_logs.txt')
    if not os.path.exists(file_path):
        return 0

    with open(file_path, 'r') as file:
        instance = int(file.read().strip())
        return instance
    
def delete_logs(experiment, algorithm):
    base_path = os.path.join(EXPERIMENT_1_DIR if experiment == 1 else EXPERIMENT_2_DIR, LOG_DIR, algorithm)
    if os.path.exists(base_path):
        for file_name in os.listdir(base_path):
            file_path = os.path.join(base_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    
