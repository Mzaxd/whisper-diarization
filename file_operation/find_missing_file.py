import os

srt_dir = 'D:\\英语资料\\EnglishPod_v3.0\\target'  # .srt文件所在的文件夹路径

start_range = 1
end_range = 365

missing_files = []  # 存放缺失文件索引的列表

for i in range(start_range, end_range + 1):
    expected_file = f"{i:03d}.mp4"
    if not os.path.exists(os.path.join(srt_dir, expected_file)):
        missing_files.append(i)  # 仅存储索引

# 打印缺失的文件索引
if missing_files:
    print("Missing file indices:", missing_files)
else:
    print("No files are missing.")
