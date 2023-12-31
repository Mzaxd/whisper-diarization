import re

def parse_srt(srt_content):
    """解析 SRT 文件内容，提取时间戳和文本"""
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n', re.DOTALL)
    entries = pattern.findall(srt_content)
    return [{'index': int(entry[0]), 'start': entry[1], 'end': entry[2], 'text': entry[3]} for entry in entries]

def time_to_seconds(time_str):
    """将时间字符串转换为秒"""
    h, m, s, ms = map(int, re.split('[:,]', time_str))
    return h * 3600 + m * 60 + s + ms / 1000.0

def seconds_to_time(seconds):
    """将秒转换回时间字符串"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

def adjust_times(srt_entries, wrapped_lines):
    """调整时间戳，并将新文本分配给相应的时间戳"""
    new_entries = []
    for entry, new_text in zip(srt_entries, wrapped_lines):
        start_seconds = time_to_seconds(entry['start'])
        end_seconds = time_to_seconds(entry['end'])
        duration = end_seconds - start_seconds

        lines = new_text.strip().split('\n')
        num_lines = len(lines)
        duration_per_line = duration / num_lines

        for i, line in enumerate(lines):
            new_start = seconds_to_time(start_seconds + i * duration_per_line)
            new_end = seconds_to_time(start_seconds + (i + 1) * duration_per_line)
            new_entries.append({'start': new_start, 'end': new_end, 'text': line})

    return new_entries

def generate_srt(entries):
    """生成新的 SRT 内容"""
    return '\n'.join([f'{i+1}\n{entry["start"]} --> {entry["end"]}\n{entry["text"]}\n' for i, entry in enumerate(entries)])

# 读取原始 SRT 文件和换行对齐的文本文件
with open('D:\\英语资料\\EnglishPod_v2.0\\test\\001.srt', 'r') as f:
    original_srt_content = f.read()

with open('D:\\英语资料\\EnglishPod_v2.0\\test\\001.txt', 'r') as f:
    wrapped_lines = f.read().split('\n\n')

# 解析原始 SRT 文件并调整时间戳
srt_entries = parse_srt(original_srt_content)
new_srt_entries = adjust_times(srt_entries, wrapped_lines)

# 生成新的 SRT 文件
new_srt_content = generate_srt(new_srt_entries)
with open('D:\\英语资料\\EnglishPod_v2.0\\test\\test.srt', 'w') as f:
    f.write(new_srt_content)
