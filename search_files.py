import os

def search_files(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if keyword in f.read():
                        matches.append(file_path)
            except Exception as e:
                # If there is an error (e.g., binary file), continue
                continue
    return matches

directory = r"D:\OneDrive - stu.hebut.edu.cn\文件\数学\HelloEthanZhou.github.io"
keyword = "feed"

matching_files = search_files(directory, keyword)
print("包含 '{}' 字段的文件在: ".format(keyword))
for file in matching_files:
    print(file)
