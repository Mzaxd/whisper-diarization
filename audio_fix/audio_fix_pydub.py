from audio_fix_pydub import AudioSegment
from audio_fix_pydub.effects import normalize

def process_audio_with_pydub(input_file, output_file):
    # 加载音频文件
    audio = AudioSegment.from_file(input_file)
    # 音频处理：例如，标准化音量
    processed_audio = normalize(audio)
    # 导出处理后的音频
    processed_audio.export(output_file, format="wav")

# 调用函数
process_audio_with_pydub("input_audio.mp3", "output_audio.wav")
