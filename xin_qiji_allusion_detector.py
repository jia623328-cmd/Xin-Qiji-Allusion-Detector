import requests
import json
import warnings
import os
warnings.filterwarnings('ignore')

def analyze_poem(poem_text, api_key):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json; charset=utf-8"  # 明确指定编码
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system", 
                "content": "分析辛弃疾词作中的历史典故，返回JSON格式"
            },
            {
                "role": "user",
                "content": poem_text
            }
        ],
        "temperature": 0.3
    }
    
    try:
        # 手动编码JSON数据
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        response = requests.post(url, headers=headers, data=json_data, verify=False, timeout=30)
        
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None

# 测试
if __name__ == "__main__":
    # 安全的使用方式
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        api_key = input("请输入您的DeepSeek API密钥: ")
    
    poem = "《永遇乐·京口北固亭怀古》..."
    result = analyze_poem(poem, api_key)
    if result:
        print("Success:", result)
    else:
        print("Failed to get result")