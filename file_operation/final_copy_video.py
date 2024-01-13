import os
import shutil
import time
import pywintypes
import win32file

def set_modification_time(file_path, new_time):
    winfile = win32file.CreateFile(
        file_path, win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE | win32file.FILE_SHARE_DELETE,
        None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None
    )

    modification_time = pywintypes.Time(new_time)
    # 设置文件的最后修改时间
    win32file.SetFileTime(winfile, None, None, modification_time)
    winfile.close()

def copy_mp4_files(source_folder, destination_folder, start_time, interval_hours, start_folder, end_folder):
    start_folder_num = int(start_folder)
    end_folder_num = int(end_folder)

    folder_names = sorted([f for f in os.listdir(source_folder) if f.isdigit() and start_folder_num <= int(f) <= end_folder_num], key=lambda x: int(x))
    current_time = start_time

    for folder_name in folder_names:
        source_path = os.path.join(source_folder, folder_name)
        mp4_files = [file for file in os.listdir(source_path) if file.endswith('.mp4')]

        if not mp4_files:
            print(f"文件夹 '{folder_name}' 中没有找到 MP4 文件。")
            continue

        for mp4_file in mp4_files:
            source_file_path = os.path.join(source_path, mp4_file)

            # 处理文件名重复情况
            destination_file_path = os.path.join(destination_folder, mp4_file)
            file_counter = 2
            while os.path.exists(destination_file_path):
                # 添加递增数字，确保文件名的唯一性
                base_name, extension = os.path.splitext(mp4_file)
                new_file_name = f"{base_name} ({file_counter}){extension}"
                destination_file_path = os.path.join(destination_folder, new_file_name)
                file_counter += 1

            try:
                shutil.copy2(source_file_path, destination_file_path)
                set_modification_time(destination_file_path, current_time)
                current_time += interval_hours * 3600

                if not os.path.isfile(destination_file_path):
                    print(f"警告：文件 '{mp4_file}' 未能成功复制到 '{destination_folder}'。")
            except Exception as e:
                print(f"错误：复制文件 '{mp4_file}' 时发生错误。错误详情：{e}")

if __name__ == "__main__":
    source_folder = r'D:\英语资料\EnglishPod_v3.0\output-fix'
    destination_folder = r'D:\英语资料\EnglishPod_v3.0\allVideo-fix'
    start_time = time.time()
    interval_hours = 1
    start_folder = '001'
    end_folder = '365'

    copy_mp4_files(source_folder, destination_folder, start_time, interval_hours, start_folder, end_folder)
