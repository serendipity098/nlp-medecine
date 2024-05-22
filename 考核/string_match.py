import json

def search_by_symptom(data, symptom):
    matched_records = []
    for record in data:
        # 检查记录中是否存在'临床表现'键
        if '临床表现' in record:
            # 检查临床表现中是否包含用户输入的病情特征
            if symptom in record['临床表现']:
                matched_records.append(record)

    return matched_records

# 用户输入的病情特征
user_input = "急性汞中毒多由职业环境引起，但也有通过皮肤黏膜以及静脉、肌内注射引起的病例报道。"

try:
    # 尝试打开并加载JSON文件
    with open('cleaned2_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: The file 'cleaned2_data.json' does not exist.")
except json.JSONDecodeError:
    print("Error: The file 'cleaned2_data.json' does not contain valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 如果没有异常发生，则执行搜索
if 'data' in locals():
    matched_data = search_by_symptom(data, user_input)
    for record in matched_data:
        print(json.dumps(record, ensure_ascii=False, indent=2))