import os
import re  # <--- 引入这个强力工具
from openai import OpenAI
from tools import write_to_file

# ---------------- 配置区域 ----------------
API_KEY = "sk-76130a52ecd54cdc847583f2cbfffa8c" # 【⚠️ 记得填 Key！】
BASE_URL = "https://api.deepseek.com"
# ----------------------------------------

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def extract_code(text):
    """
    终极版提取器：使用正则表达式。
    不管 AI 怎么罗嗦，只抓取 ``` ... ``` 中间的内容。
    如果有多个代码块，自动抓取最长的那一段（通常是主代码）。
    """
    # 这里的正则意思是：寻找 ```(任意语言名) (中间所有内容) ```
    pattern = r"```(?:\w+)?\s*(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    
    if matches:
        # 找到最长的一段代码返回（防止它先写了一段简短的演示，后写正文）
        return max(matches, key=len).strip()
    
    # 兜底：如果真没找到 ```，就把所有文字里的 "import" 等废话去掉试试，或者直接返回
    return text.strip()

def coder_agent(task_prompt, file_path):
    print(f"👷 程序员 Agent 正在处理文件：{file_path}")
    print(f"Thinking...")

    file_name = os.path.basename(file_path)
    file_ext = os.path.splitext(file_path)[1]
    
    # 升级版指令：明确告诉它文件之间的引用关系
    system_prompt = f"""
    你是一个 Web 全栈专家。
    任务：编写 {file_name}。
    
    【关键引用规则】：
    1. 所有的文件 (index.html, style.css, script.js) 都在同一个文件夹下。
    2. 在 html 引入 css 时，请使用 <link rel="stylesheet" href="style.css"> (不要加 workspace/)
    3. 在 html 引入 js 时，请使用 <script src="script.js"></script> (不要加 workspace/)
    
    【格式规则】：
    1. 只输出代码，包裹在 ```{file_ext.replace('.', '')} 和 ``` 之间。
    2. HTML 必须包含 <!DOCTYPE html> 骨架。
    3. JS 必须包含 window.onload 或 DOMContentLoaded 事件，确保页面加载完再执行。
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": task_prompt}
            ],
            stream=False
        )
        
        full_reply = response.choices[0].message.content
        code = extract_code(full_reply)
        
        # 再次清洗：有时候代码开头会有 'html' 字样残留
        if code.startswith("html"): code = code[4:]
        if code.startswith("css"): code = code[3:]
        if code.startswith("javascript"): code = code[10:]
        if code.startswith("js"): code = code[2:]
        
        result = write_to_file(file_path, code)
        print(f"✅ 文件生成完毕：{result}")
        
    except Exception as e:
        print(f"❌ 出错了：{e}")