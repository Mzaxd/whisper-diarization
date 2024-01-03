import requests
import os
import re
import json
import time

# 源目录和目标目录路径
source_dir = r"D:\英语资料\EnglishPod_v3.0\source"
target_dir = r"D:\英语资料\EnglishPod_v3.0\target"

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)


# 定义替换函数
def replace_speaker_names(text, speaker_names):
    for key, value in speaker_names.items():
        text = text.replace(key + ":", f"{value}:")  # 添加冒号以确保不会替换错误的文本
    return text


# 从API获取说话人名字的映射
def get_speaker_names(file_content):
    API_URL = "https://flowise.elizaveta.top:700/api/v1/prediction/797ea971-3f6e-4d04-9014-4cdfec70248d"
    payload = {"question": file_content}
    response = requests.post(API_URL, json=payload)

    print(response)
    response_text = response.json()
    print(response_text)
    try:
        # 使用正则表达式找到JSON字符串
        json_str_match = re.search(r'```json\n({.*?})\n```', response_text, re.DOTALL)
        if json_str_match:
            # 提取JSON字符串并解析为字典
            json_str = json_str_match.group(1)
            speaker_names = json.loads(json_str)
            return speaker_names
    except Exception as e:
        print(f"An error occurred while parsing the JSON data: {e}")
    return None


# 指定处理的文件范围
start_file_number = 201
end_file_number = 365

file_indices = [218, 348]

# 格式化文件名，并遍历指定范围内的文件编号
for file_number in range(start_file_number, end_file_number + 1):
# for file_number in file_indices:
    file_base_name = f"{file_number:03}"  # 文件名格式为001, 002, ... 100
    txt_file_name = file_base_name + ".txt"
    txt_file_path = os.path.join(source_dir, txt_file_name)

    if os.path.exists(txt_file_path):
        # 读取.txt文件内容
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # 使用文件内容作为API的请求参数
        speaker_names = get_speaker_names(file_content)

        # 如果获取到映射，开始处理文件
        if speaker_names:
            # 对于每个编号处理.txt和.srt文件
            for ext in ('.srt', '.txt'):
                src_file_path = os.path.join(source_dir, file_base_name + ext)
                if os.path.exists(src_file_path):
                    # 读取原始文件内容
                    with open(src_file_path, 'r', encoding='utf-8') as src_file:
                        content = src_file.read()

                    # 替换说话人名
                    replaced_content = replace_speaker_names(content, speaker_names)

                    # 构建目标文件路径
                    target_file_path = os.path.join(target_dir, file_base_name + ext)

                    # 写入替换后的内容到目标文件
                    with open(target_file_path, 'w', encoding='utf-8') as target_file:
                        target_file.write(replaced_content)
                    print(f"Processed and saved: {target_file_path}")
        else:
            print(f"Failed to retrieve speaker names for {txt_file_name}.")

    time.sleep(1)
