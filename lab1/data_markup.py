import os
import shutil

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, 'data')
all_data = [
    file
    for file in os.listdir(DATA_PATH)
]
not_murk_up_file = [
    file
    for file in all_data
    if '_' not in file
]

print(f'Всего файлов: {len(all_data)}')
print(f'Не размеченных: {len(not_murk_up_file)}')

RANGES_TO_FLAGS = {
    0: (
        (36, 80),
        (356, 420),
        (501, 830)
    ),
    1: (
        (1, 35),
        (81, 355),
        (420, 500)
    )
}


def get_name(number: int) -> str:
    return f'{str(number).zfill(4)}.jpg'


for flag, ranges in RANGES_TO_FLAGS.items():
    flag_counter = 0
    for start, end in ranges:
        for number in range(start, end + 1):
            prev_name, prev_ext = get_name(number).split('.')
            new_name = f"flag_{prev_name}.{prev_ext}"
            os.rename(f'{prev_name}.{prev_ext}', new_name)
            flag_counter += 1
