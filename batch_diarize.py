import subprocess
import os
import time

# 设置变量
diarize_script = './diarize.py'
audio_dir = 'D:\\英语资料\\EnglishPod_v2.0\\audio'
venv_python = 'D:\\Code\\PythonProject\\whisper-diarization\\venv\\Scripts\\python'  # Windows路径
total_files = len(os.listdir(audio_dir))
whisper_model = 'medium.en'
suppress_numerals = True

# 总执行时间和命令执行时间列表
total_execution_time = 0
execution_times = []

# 打印任务开始时间
task_start_time = time.time()
print(f"Task started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(task_start_time))}")

end = 5
audio_indices = [89]

# 循环执行命令
# for i in range(5, end + 1):
for i in audio_indices:
    # 构建音频文件名
    audio_file_name = f"{i:03d}.wav"
    audio_file_path = os.path.join(audio_dir, audio_file_name)

    # 构建命令，使用虚拟环境的Python解释器
    command = [
        venv_python, diarize_script,
        '-a', audio_file_path,
        '--whisper-model', whisper_model,
        '--no-stem'
    ]
    if suppress_numerals:
        command.append('--suppress_numerals')

    # 记录单个命令的开始时间
    command_start_time = time.time()

    # 执行命令
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='ignore')

    # 记录单个命令的结束时间和执行时间
    command_end_time = time.time()
    command_execution_time = command_end_time - command_start_time
    execution_times.append(command_execution_time)

    print(f"Command for {audio_file_name} executed in {command_execution_time:.2f} seconds.")

    # 输出结果
    if result.returncode == 0:
        print(f"Output:\n{result.stdout}")
    else:
        print(f"Error:\n{result.stderr}")

# 计算和打印总执行时间、任务结束时间和平均执行时间
total_execution_time = sum(execution_times)
task_end_time = time.time()
average_execution_time = total_execution_time / total_files

print(f"Task ended at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(task_end_time))}")
print(f"All commands have been executed in {total_execution_time:.2f} seconds.")
print(f"Average execution time per command was {average_execution_time:.2f} seconds.")
