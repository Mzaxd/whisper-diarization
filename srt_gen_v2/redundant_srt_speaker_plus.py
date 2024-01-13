import os
import re


def remove_redundant_speakers(srt_text):
    lines = srt_text.strip().split('\n')
    processed_lines = []
    previous_speaker = None

    for i in range(len(lines)):
        line = lines[i]
        # 检查当前行是否包含时间戳
        if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line):
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # 检查下一行是否包含发言者标记
                if ':' in next_line:
                    current_speaker = next_line.split(':')[0]
                    if current_speaker == previous_speaker:
                        # 移除发言者标记
                        lines[i + 1] = ':'.join(next_line.split(':')[1:]).strip()
                    else:
                        previous_speaker = current_speaker
        processed_lines.append(line)

    return '\n'.join(processed_lines)


def process_srt_file(file_path):
    # Read the SRT file
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_text = file.read()

    # Process the SRT text
    processed_text = remove_redundant_speakers(srt_text)

    # Overwrite the original file with the processed text
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_text)

    return "File processed and saved at: " + file_path


def process_srt_files_in_directory(directory_path):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        # 检查文件扩展名是否为.srt
        if filename.endswith('.srt'):
            # 构造完整的文件路径
            file_path = os.path.join(directory_path, filename)
            # 处理文件
            process_srt_file(file_path)
            print(f"Processed file: {file_path}")


# 替换为您的目录路径
directory_path = 'D:\\英语资料\\EnglishPod_v3.0\\target-fix'
process_srt_files_in_directory(directory_path)
