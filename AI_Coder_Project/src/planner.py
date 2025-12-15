import json
from openai import OpenAI

# ---------------- 配置区域 ----------------
API_KEY = "" # 【记得换成你的 Key】
BASE_URL = "https://api.deepseek.com"
# ----------------------------------------

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def planner_agent(requirement):
    print(f"🧐 项目经理 Agent 收到需求：{requirement}")
    print(f"Thinking...")

    # 1. 设定人设
    # 我们要求它必须输出 JSON 格式，这样程序才能自动读取文件名
    system_prompt = """
    你是一个资深软件架构师。
    你的任务是将用户的需求拆解为具体的文件列表。
    
    请只输出一个 JSON 列表，格式如下，不要包含任何其他废话：
    [
        {
            "file": "文件名 (例如 index.html)",
            "instruction": "这个文件具体的代码编写要求..."
        },
        {
            "file": "另一个文件名",
            "instruction": "另一个文件的要求..."
        }
    ]
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"项目需求：{requirement}"}
            ],
            stream=False
        )
        
        # 2. 获取回复
        content = response.choices[0].message.content
        
        # 清理一下可能多余的符号（比如 ```json ... ```）
        content = content.replace("```json", "").replace("```", "").strip()
        
        # 3. 把文字转换成 Python 列表 (JSON 解析)
        plan = json.loads(content)
        
        print(f"✅ 计划制定完成！共拆解为 {len(plan)} 个文件。")
        return plan

    except Exception as e:
        print(f"❌ 计划制定失败：{e}")
        # 如果出错，返回一个空列表
        return []

# --- 测试一下 ---
if __name__ == "__main__":
    # 测试任务：做一个简单的个人主页
    task = "帮我做一个简单的个人主页，包含一个 index.html 和一个 style.css"
    
    plan_list = planner_agent(task)
    
    # 打印看看计划是什么样子的
    for item in plan_list:
        print(f"📄 待办文件: {item['file']}")
        print(f"   指令: {item['instruction'][:50]}...") # 只打印前50个字