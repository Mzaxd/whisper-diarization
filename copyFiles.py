import os
import shutil


def copy_files(source_folder, target_folder, file_pattern):
    """
    Copies files from source folder to target folder based on a naming pattern.

    :param source_folder: Path to the source folder
    :param target_folder: Path to the target folder
    :param file_pattern: File naming pattern (e.g., '001.txt', '002.txt', ...)
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for i in range(365, 366):  # Assuming a maximum of 999 files
        file_name = file_pattern.format(i)
        source_file = os.path.join(source_folder, file_name)
        target_file = os.path.join(target_folder, file_name)

        if os.path.exists(source_file):
            shutil.copy(source_file, target_file)
            print(f"Copied {file_name}")
        else:
            print(f"File {file_name} not found in source folder.")


# Example usage
source_folder = 'D:\\英语资料\\EnglishPod_v2.0\\source'
target_folder = 'D:\\英语资料\\EnglishPod_v2.0\\source2'
file_pattern = '{:03d}.txt'  # For files like 001.txt, 002.txt, ...

copy_files(source_folder, target_folder, file_pattern)
