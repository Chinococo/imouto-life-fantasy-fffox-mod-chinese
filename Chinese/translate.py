import os

# 設定特定的關鍵字
keyword = "Sh"


# 定義遞迴函數來遍歷目錄
def search_files(directory):
    #print(directory)
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                #print(file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # 檢查文件中是否包含關鍵字
                if keyword in content:
                    print(f"找到關鍵字的文件: {file_path}")

        # 遞迴遍歷子目錄
        for dir in dirs:
            search_files(os.path.join(root, dir))


# 從當前目錄開始搜索
search_files('.')

print("所有包含關鍵字的文件已經查找完成。")
