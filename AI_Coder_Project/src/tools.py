import os

# 1. 写文件工具：把内容写入指定路径
def write_to_file(filename, content):
    try:
        # 确保文件的父目录存在，如果不存在就自动创建
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # 打开文件并写入（'w'表示覆盖写入，'utf-8'防止中文乱码）
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"成功：文件 '{filename}' 已保存。"
    except Exception as e:
        return f"失败：写入文件时出错。错误信息：{e}"

# 2. 读文件工具：读取指定路径的内容
def read_file(filename):
    try:
        if not os.path.exists(filename):
            return f"失败：找不到文件 '{filename}'"
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"失败：读取文件时出错。错误信息：{e}"

# --- 下面是测试代码，只有直接运行这个文件时才会执行 ---
if __name__ == "__main__":
    # 测试一下我们的机械手好不好用
    print("正在测试机械手...")
    
    # 试着写一个文件
    path = "test_folder/hello.txt"
    result = write_to_file(path, "你好！这是 AI 的机械手写下的第一行字。")
    print(result)
    
    # 试着读回来
    content = read_file(path)
    print(f"读到的内容是：{content}")