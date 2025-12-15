from openai import OpenAI

# ----------------------------------------------------
# 请小心替换下面引号里的内容，保留双引号
my_api_key = "sk-76130a52ecd54cdc847583f2cbfffa8c" 
# ----------------------------------------------------

client = OpenAI(
    api_key=my_api_key, 
    base_url="https://api.deepseek.com"
)

print("正在呼叫 DeepSeek 大脑...")

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个非常有用的编程助手。"},
            {"role": "user", "content": "你好！请用一句话告诉我，什么是 Agent？"}
        ],
        stream=False
    )
    print("\n连接成功！DeepSeek 回复说：")
    print("-" * 30)
    print(response.choices[0].message.content)
    print("-" * 30)

except Exception as e:
    print("出错了！")
    print(e)