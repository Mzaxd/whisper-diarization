from spleeter.separator import Separator
import multiprocessing
import tensorflow as tf


def separate_audio(input_file, output_path):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_file, output_path, duration=1000.0)


def main():
    # 调用多进程相关的函数
    separate_audio('D:\\英语资料\\EnglishPod_v2.0\\audio\\018.wav', 'D:\\英语资料\\EnglishPod_v2.0\\test')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    tf.config.list_physical_devices('GPU')
    print('GPU加速可用:')
    print(tf.test.is_gpu_available())
    main()
