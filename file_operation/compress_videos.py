import os
import subprocess
import time


def get_file_modification_time(file_path):
    try:
        modification_time = os.path.getmtime(file_path)
        return modification_time
    except Exception as e:
        print(f"Error getting modification time for {file_path}: {e}")
        return 0


def compress_videos(input_folder_path, output_folder_path, target_bitrate="1M", crf_value=23, resolution="1920:1080"):
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 获取文件列表并按照修改时间排序
    files = [(f, get_file_modification_time(os.path.join(input_folder_path, f))) for f in os.listdir(input_folder_path)
             if f.endswith(".mp4")]
    files.sort(key=lambda x: x[1])  # 根据修改时间排序

    # 遍历排序后的文件列表
    for filename, _ in files:
        # 构建原始视频和输出视频的完整路径
        original_video = os.path.join(input_folder_path, filename)
        compressed_video = os.path.join(output_folder_path, filename)

        # 构建ffmpeg命令
        command = [
            "ffmpeg",
            "-i", original_video,  # 输入文件
            "-c:v", "h264_nvenc",  # 使用NVIDIA硬件加速编码
            "-rc", "vbr",  # 变比特率模式
            "-cq", str(crf_value),  # 设置CRF值
            "-b:v", target_bitrate,  # 设置目标码率
            "-vf", f"scale={resolution}",  # 设置目标分辨率
            compressed_video  # 输出文件
        ]

        try:
            # 执行命令
            subprocess.run(command, check=True)
            print(f"Compressed: {filename}")
        except subprocess.CalledProcessError as e:
            # 如果发生错误，打印出来
            print(f"Error compressing {filename}: {e}")


if __name__ == "__main__":
    input_folder_path = "D:\\英语资料\\EnglishPod_v3.0\\allVideo-fix"
    output_folder_path = "D:\\英语资料\\EnglishPod_v3.0\\CompressedVideos"
    compress_videos(input_folder_path, output_folder_path, target_bitrate="5M", crf_value=23, resolution="1920:1080")
