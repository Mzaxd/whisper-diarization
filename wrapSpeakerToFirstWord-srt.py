import os


def abbreviate_speaker_names(srt_content):
    """
    Function to abbreviate speaker names in SRT content to their initials.
    """
    updated_lines = []
    for line in srt_content.split('\n'):
        if ':' in line and not '-->' in line:  # Check for speaker lines and exclude timestamp lines
            speaker, speech = line.split(':', 1)
            initials = ''.join([word[0] for word in speaker.split()])
            updated_line = f"{initials}:{speech}"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    return '\n'.join(updated_lines)


def abbreviate_speaker_names_in_file(file_path):
    """
    Function to read an SRT file, abbreviate speaker names, and overwrite the file with modified content.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    abbreviated_content = abbreviate_speaker_names(content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(abbreviated_content)


def process_srt_files_in_directory(directory_path):
    """
    Function to process all SRT files in a given directory.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith('.srt'):
            file_path = os.path.join(directory_path, filename)
            abbreviate_speaker_names_in_file(file_path)
            print(f"Processed {filename}")


# Example usage
directory_path = '/path/to/your/srt/files'  # Replace with your directory path
process_srt_files_in_directory(directory_path)
