import os
import shutil
import time


def copy_mp4_files(source_folder, destination_folder):
    # 获取源文件夹中所有文件夹的名称
    folder_names = sorted(os.listdir(source_folder))

    for folder_name in folder_names:
        # 构建源文件夹路径
        source_path = os.path.join(source_folder, folder_name)

        # 获取源文件夹中的所有mp4文件
        mp4_files = [file for file in os.listdir(source_path) if file.endswith('.mp4')]

        for mp4_file in mp4_files:
            source_file_path = os.path.join(source_path, mp4_file)
            destination_file_path = os.path.join(destination_folder, mp4_file)

            # 复制文件
            shutil.copy2(source_file_path, destination_file_path)

            # 暂停1秒钟
            time.sleep(1)


if __name__ == "__main__":
    source_folder = r'D:\英语资料\EnglishPod_v3.0\output'  # 指定源文件夹路径
    destination_folder = r'D:\英语资料\EnglishPod_v3.0\allVideo'  # 指定目标文件夹路径

    copy_mp4_files(source_folder, destination_folder)
