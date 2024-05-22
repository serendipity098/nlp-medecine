import json
import re

# 假设这是原始JSON文件的路径
original_json_file_path = 'cleaned1_data.json'

# 假设这是新JSON文件的路径
new_json_file_path = 'cleaned2_data.json'

# 读取原始JSON文件
with open(original_json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 检查data是否是列表，且列表中的元素都是字典
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    # 遍历列表，除了最后一个元素
    for i in range(len(data) - 1):
        # 获取当前元素的"处理原则"的值
        current_principle = data[i].get("处理原则", "")
        
        # 获取下一个元素的"id"的值，并转义正则表达式特殊字符
        next_id = re.escape(data[i + 1].get("id", ""))
        
        # 使用正则表达式替换，移除当前"处理原则"中包含的下一个"id"的内容
        current_principle = re.sub(next_id, "", current_principle)
        
        # 更新当前元素的"处理原则"
        data[i]["处理原则"] = current_principle

# 将修改后的数据保存到新的JSON文件中
with open(new_json_file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# 打印新文件的路径，以确认保存成功
print(f'Processed data has been saved to {new_json_file_path}')
