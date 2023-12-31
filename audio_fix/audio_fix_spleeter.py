from spleeter.separator import Separator
import multiprocessing

def separate_audio(input_file, output_path):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_file, output_path, duration=1200.0)

def main():
    # 调用多进程相关的函数
    separate_audio('D:\\英语资料\\EnglishPod_v2.0\\audio\\018.wav', 'D:\\英语资料\\EnglishPod_v2.0\\test')

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
