import audoi_fix_numpy as np
from scipy.io import wavfile
from scipy.fft import fft, ifft

def reduce_noise_fft(audio_path, output_path):
    # 读取音频文件
    sr, data = wavfile.read(audio_path)
    # FFT变换
    fft_data = fft(data)
    # 噪声减少：例如，移除频率幅度较小的部分
    threshold = np.max(np.abs(fft_data)) / 10
    fft_data[np.abs(fft_data) < threshold] = 0
    # 反FFT变换
    clean_data = ifft(fft_data).real
    # 保存音频文件
    wavfile.write(output_path, sr, clean_data.astype(np.int16))

# 调用函数
reduce_noise_fft('input_audio.wav', 'output_audio.wav')
