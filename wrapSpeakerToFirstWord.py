import os

def process_dialogue(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        colon_index = line.find(':')
        if colon_index != -1:
            # 提取说话人和对话内容
            speaker = line[:colon_index].strip()
            speech = line[colon_index + 1:]
            # 获取说话人的首字母
            initials = ''.join([word[0] for word in speaker.split()])
            # 重构行
            new_line = initials + ':' + speech
            processed_lines.append(new_line)
        else:
            processed_lines.append(line)

    # 将处理后的内容存储在变量中
    processed_content = ''.join(processed_lines)

    # 将处理后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

def process_all_files(directory):
    for i in range(1, 366):
        file_name = f"{i:03}.txt"
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            process_dialogue(file_path)
        else:
            print(f"File not found: {file_path}")

# 替换为您的目录路径
directory = "D:\\英语资料\\EnglishPod_v2.0\\source"
process_all_files(directory)
