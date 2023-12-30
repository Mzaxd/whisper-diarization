import os

def remove_empty_first_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if lines:
        first_line = lines[0]
        if ':' in first_line and not first_line.split(':', 1)[1].strip():
            lines = lines[1:]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and filename[:3].isdigit():
            file_path = os.path.join(folder_path, filename)
            remove_empty_first_line(file_path)

# 使用方法
folder_path = 'D:\\英语资料\\EnglishPod_v2.0\\source'  # 替换为您的文件夹路径
process_folder(folder_path)
