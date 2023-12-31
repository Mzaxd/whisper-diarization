import os

def clean_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    valid_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().isdigit():
            # 检查对话内容是否为空
            if i + 2 < len(lines) and ':' in lines[i + 2] and not lines[i + 2].split(':', 1)[1].strip():
                i += 3  # 跳过无效片段
            else:
                # 添加有效片段
                valid_lines.extend(lines[i:i+3])
                i += 3
        else:
            # 添加空行和其他非字幕片段的行
            valid_lines.append(lines[i])
            i += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(valid_lines)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.srt'):
            file_path = os.path.join(folder_path, filename)
            clean_srt(file_path)

# 使用方法
folder_path = 'D:\\英语资料\\EnglishPod_v2.0\\source'  # 替换为您的文件夹路径
process_folder(folder_path)
