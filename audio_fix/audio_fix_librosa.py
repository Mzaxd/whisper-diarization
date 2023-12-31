import audio_fix_librosa
import audoi_fix_numpy as np
import scipy.signal

def reduce_noise(audio_path, output_path):
    # 加载音频文件
    y, sr = librosa.load(audio_path, sr=None)

    # 简单的噪声减少处理：我们可以使用一个低通滤波器
    # 例如，设计一个简单的窗函数低通滤波器
    n = 15  # 滤波器的长度
    b = scipy.signal.firwin(n, cutoff=0.5, window="hamming")

    # 应用滤波器
    y_filtered = scipy.signal.lfilter(b, [1.0], y)

    # 将处理后的音频保存到输出路径
    librosa.output.write_wav(output_path, y_filtered, sr)

# 调用函数
reduce_noise("path_to_your_input_audio.wav", "path_to_your_output_audio.wav")
