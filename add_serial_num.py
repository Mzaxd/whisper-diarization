# 指定输入文件和输出文件
input_file = 'D:\\英语资料\\EnglishPod_v2.0\\java_version\\allTitle.txt'
output_file = 'D:\\英语资料\\EnglishPod_v2.0\\java_version\\output.txt'

# 打开输入文件以及输出文件
with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
    # 初始化行号
    line_number = 1

    # 逐行处理文件内容
    for line in input_f:
        # 添加序号并写入输出文件
        output_line = f"{line_number}: {line}"
        output_f.write(output_line)

        # 增加行号
        line_number += 1

print("添加序号完成")
