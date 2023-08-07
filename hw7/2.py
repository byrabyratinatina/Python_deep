from pathlib import Path
import os


def rename(end_name: str, count_sequence_number: int, start_extensions: str,
           end_expansions: str, slice_name: list[int, int], directory=Path().cwd()):
    start_number = 1
    start_slice, end_slice = slice_name
    for dirs, folders, files in os.walk(directory):
        for i, file in enumerate(files):
            if file.endswith(start_extensions):
                old_name = Path(dirs) / file
                old_name.rename(
                    f'{dirs}/{file[start_slice:end_slice]}{end_name}{str(start_number).zfill(count_sequence_number)}.{end_expansions}')
                start_number += 1


rename('new', 3, 'txt', 'doc', [0, 5], 'Test_folder_file')
