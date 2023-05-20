import os
from web5_5 import extract_tags_from_files, save_tags_to_excel

# 매개변수 설정
folder_path = "./"

# 폴더 내의 txt 파일 탐색
txt_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))

# HTML 코드에서 중복되는 태그 추출
tags = extract_tags_from_files(txt_files)

# 엑셀로 저장
filename = "tags.xlsx"
save_tags_to_excel(tags, filename)