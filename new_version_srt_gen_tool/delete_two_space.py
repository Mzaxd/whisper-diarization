import os


# 定义处理文本的函数
def process_text_file(input_file):
    try:
        with open(input_file, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            file.seek(0)  # 将文件指针移到文件开头
            file.truncate()  # 清空文件内容
            for line in lines:
                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        first_part = parts[0].strip()
                        second_part = parts[1].strip()
                        output_line = f"{first_part}: {second_part}\n"
                        file.write(output_line)
                else:
                    file.write(line)
        print(f"处理完成: {input_file}")
    except Exception as e:
        print(f"处理文本时出现错误: {str(e)}")


# 指定文件夹路径
folder_path = 'D:\\英语资料\\EnglishPod_v2.0\\source'

# 获取文件夹中的所有txt文件
file_list = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.txt')]

# 遍历文件列表
for file_name in file_list:
    # 构建输入文件的完整路径
    input_file_path = os.path.join(folder_path, file_name)

    # 调用处理函数
    process_text_file(input_file_path)
