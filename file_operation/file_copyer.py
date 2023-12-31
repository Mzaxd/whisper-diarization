import os
import shutil
from mutagen.mp3 import MP3
from pydub import AudioSegment

source_dir = 'D:\\英语资料\\EnglishPod.365.Collective'
destination_dir = 'D:\\英语资料\\EnglishPod_v2.0\\audio'
file_counter = 1  # 用于文件重命名的计数器

# 确保目标文件夹存在
os.makedirs(destination_dir, exist_ok=True)

# 遍历源目录
for folder_range in os.listdir(source_dir):
    range_path = os.path.join(source_dir, folder_range)

    # 确保它是一个文件夹
    if os.path.isdir(range_path):
        for subfolder in os.listdir(range_path):
            subfolder_path = os.path.join(range_path, subfolder)

            # 选择时长最长的MP3文件
            longest_file = None
            longest_duration = 0
            for file in os.listdir(subfolder_path):
                if file.endswith('.mp3'):
                    file_path = os.path.join(subfolder_path, file)
                    audio = MP3(file_path)
                    duration = audio.info.length  # 获取MP3文件的时长
                    if duration > longest_duration:
                        longest_file = file
                        longest_duration = duration

            # 如果找到了MP3文件，将其复制到目标文件夹并重命名
            if longest_file:
                longest_file_path = os.path.join(subfolder_path, longest_file)
                new_file_name = f"{file_counter:03d}.mp3"  # 生成新的文件名，如001.mp3, 002.mp3等
                destination_file_path = os.path.join(destination_dir, new_file_name)

                # 复制文件
                shutil.copy2(longest_file_path, destination_file_path)
                print(f"Copied {longest_file} to {destination_file_path} with duration {longest_duration} seconds.")

                # 增加计数器以用于下一个文件的命名
                file_counter += 1

print("All files have been copied successfully.")
