import os

# 设置文件夹路径
srt_dir = 'D:\\英语资料\\EnglishPod_v2.0\\audio'  # 请替换为您的.srt文件所在的文件夹路径

# 设置预期的文件范围
start_range = 1
end_range = 365

# 存放缺失文件索引的列表
missing_files = []

# 检查文件夹内的每一个文件
for i in range(start_range, end_range + 1):
    expected_file = f"{i:03d}.srt"
    if not os.path.exists(os.path.join(srt_dir, expected_file)):
        missing_files.append(expected_file)

# 打印缺失的文件
if missing_files:
    print("Missing files:")
    for file_name in missing_files:
        print(file_name)
else:
    print("No files are missing.")
