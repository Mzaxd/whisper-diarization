import os


def remove_redundant_speakers(srt_text):
    # Split the text into lines
    lines = srt_text.strip().split('\n')

    # Initialize variables
    previous_speaker = None
    processed_lines = []

    # Process each line
    for line in lines:
        # Check if the line contains a speaker
        if line.startswith("Speaker"):
            current_speaker = line.split(':')[0]  # Get the speaker's name/number
            if current_speaker == previous_speaker:
                # Remove the speaker if it's the same as the previous one
                line = ':'.join(line.split(':')[1:]).strip()
            else:
                # Update the previous speaker
                previous_speaker = current_speaker
        # Add the line to the processed lines
        processed_lines.append(line)

    # Join the processed lines back into a single string
    return '\n'.join(processed_lines)


def process_srt_file(file_path):
    # Read the SRT file
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_text = file.read()

    # Process the SRT text
    processed_text = remove_redundant_speakers(srt_text)

    # Overwrite the original file with the processed text
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_text)

    return "File processed and saved at: " + file_path


def process_srt_files_in_directory(directory_path):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory_path):
        # 检查文件扩展名是否为.srt
        if filename.endswith('.srt'):
            # 构造完整的文件路径
            file_path = os.path.join(directory_path, filename)
            # 处理文件
            process_srt_file(file_path)
            print(f"Processed file: {file_path}")


# 替换为您的目录路径
directory_path = 'D:\\英语资料\\EnglishPod_v3.0\\source'
process_srt_files_in_directory(directory_path)
