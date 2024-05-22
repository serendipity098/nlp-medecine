import json

# 假设原始JSON文件名为 'data.json'
input_filename = 'cleaned2_data.json'
output_filename = 'cleaned3_data.json'

# 读取原始JSON文件
with open(input_filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化一个集合来存储已经见过的id（忽略空格）
seen_ids = set()
# 初始化一个列表来存储去重后的数据
unique_data = []

# 遍历原始数据中的每个元素
for item in data:
    # 检查item是否包含'id'键
    if 'id' in item:
        # 去除id两边的空格
        clean_id = item['id'].strip()
        # 如果clean_id不在seen_ids中，则添加到unique_data和seen_ids
        if clean_id not in seen_ids:
            unique_data.append(item)
            seen_ids.add(clean_id)
    else:
        # 如果item不包含'id'键，直接添加到unique_data
        unique_data.append(item)

# 将去重后的数据写入新的JSON文件
with open(output_filename, 'w', encoding='utf-8') as file:
    json.dump(unique_data, file, ensure_ascii=False, indent=4)

print(f"去重后的JSON数据已保存到 '{output_filename}'")