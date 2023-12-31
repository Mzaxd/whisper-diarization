import os
import chardet

def detect_encoding(file_path):
    """
    Detects the encoding of a given file.
    :param file_path: Path to the file
    :return: Detected encoding
    """
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def convert_to_utf8(source_folder):
    """
    Converts all .txt and .srt files in a folder to UTF-8 encoding.
    :param source_folder: Path to the source folder
    """
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.txt') or file_name.endswith('.srt'):
            file_path = os.path.join(source_folder, file_name)
            encoding = detect_encoding(file_path)

            # Only convert if the encoding is not already UTF-8
            if encoding != 'utf-8':
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        content = file.read()
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f"Converted {file_name} from {encoding} to UTF-8")
                except Exception as e:
                    print(f"Error converting {file_name}: {e}")

# Example usage
source_folder = 'D:\\英语资料\\EnglishPod_v3.0\\target'  # Replace with your folder path
convert_to_utf8(source_folder)
