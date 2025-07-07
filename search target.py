import os


def find_files_with_categories(folder_path):
    """查找指定文件夹中同时包含0、1、2类别的txt文件"""
    result_files = []

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            # 检查是否为txt文件
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)

                # 初始化类别集合
                categories = set()

                # 读取文件内容
                try:
                    with open(file_path, 'r') as f:
                        for line in f:
                            # 分割每行数据
                            parts = line.strip().split()
                            if parts:  # 确保行不为空
                                # 获取类别（每行的第一个元素）
                                category = parts[0]
                                categories.add(category)

                                # 如果已找到所有需要的类别，提前结束循环
                                if {'0', '1', '2'}.issubset(categories):
                                    break
                except Exception as e:
                    print(f"读取文件 {file_path} 时出错: {e}")
                    continue

                # 检查是否同时包含0、1、2类别
                if {'0', '1', '2'}.issubset(categories):
                    result_files.append(file_path)

    return result_files


if __name__ == "__main__":
    # 指定要搜索的文件夹路径
    folder_path = input("请输入要搜索的文件夹路径: ")

    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误: 文件夹 '{folder_path}' 不存在")
    else:
        # 查找符合条件的文件
        files = find_files_with_categories(folder_path)

        # 输出结果
        if files:
            print(f"找到 {len(files)} 个同时包含0、1、2类别的txt文件:")
            for file in files:
                print(file)
        else:
            print("未找到同时包含0、1、2类别的txt文件")
