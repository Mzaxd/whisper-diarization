import re
from datetime import datetime, timedelta
from pathlib import Path


def parse_srt(srt_content):
    """ 解析 SRT 文件内容，提取时间标签和文本。"""
    entries = re.split(r'\n\n+', srt_content.strip())
    srt_data = []
    for entry in entries:
        lines = entry.split('\n')
        if len(lines) >= 3:
            time_range = lines[1]
            text = ' '.join(lines[2:])
            srt_data.append((time_range, text))
    return srt_data

def calculate_time_segments(time_range, num_segments):
    """ 将给定的时间范围分成多个段。"""
    start_str, end_str = time_range.split(' --> ')
    start = datetime.strptime(start_str.strip(), '%H:%M:%S,%f')
    end = datetime.strptime(end_str.strip(), '%H:%M:%S,%f')
    delta = (end - start) / num_segments
    segments = []
    for i in range(num_segments):
        segment_start = start + delta * i
        segment_end = segment_start + delta
        segments.append(f"{segment_start.strftime('%H:%M:%S,%f')[:-3]} --> {segment_end.strftime('%H:%M:%S,%f')[:-3]}")
    return segments

def create_new_srt(srt_data, aligned_paragraphs):
    """ 生成新的 SRT 文件内容。"""
    new_srt_content = []
    srt_index = 1
    for (time_range, _), paragraph in zip(srt_data, aligned_paragraphs):
        lines = paragraph.split('\n')
        time_segments = calculate_time_segments(time_range, len(lines))
        for line, segment in zip(lines, time_segments):
            new_srt_content.append(f"{srt_index}\n{segment}\n{line}")
            srt_index += 1
    return '\n\n'.join(new_srt_content)

def process_folder(folder_path):
    """ 批量处理指定文件夹下的所有 SRT 和 TXT 文件。"""
    for path in Path(folder_path).glob('*.srt'):
        srt_filename = path.stem
        txt_filename = f"{srt_filename}.txt"
        txt_path = path.with_name(txt_filename)

        if txt_path.exists():
            with open(path, 'r', encoding='utf-8') as srt_file:
                srt_content = srt_file.read()
            with open(txt_path, 'r', encoding='utf-8') as txt_file:
                aligned_text = txt_file.read()

            srt_data = parse_srt(srt_content)
            aligned_paragraphs = aligned_text.strip().split('\n\n')
            new_srt = create_new_srt(srt_data, aligned_paragraphs)

            new_srt_path = path.with_name(f"{srt_filename}_processed.srt")
            with open(new_srt_path, 'w', encoding='utf-8') as new_srt_file:
                new_srt_file.write(new_srt)
            print(f"Processed {srt_filename}.srt")

folder_path = 'D:\\英语资料\\EnglishPod_v2.0\\source'  # 将此路径替换为您的文件夹路径
process_folder(folder_path)
