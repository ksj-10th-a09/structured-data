import os
import pandas as pd
from bs4 import BeautifulSoup

# 탐색할 폴더 경로
folder_path = "./"

# 폴더 내의 txt 파일 탐색
txt_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(os.path.join(root, file))

# HTML 코드에서 중복되는 태그 추출
tags = set()
for txt_file in txt_files:
    with open(txt_file, "r", encoding="utf-8") as f:
        html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all():
            tags.add(tag.name)

# 중복 태그 처리 후 추출된 태그를 데이터프레임으로 변환
df = pd.DataFrame({"Tag": list(tags)})

# 엑셀로 저장
filename = "tags.xlsx"
df.to_excel(filename, index=False)

print(f"Tags have been saved to {filename}")