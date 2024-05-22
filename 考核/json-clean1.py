import json
import re

# 读取原始 JSON 文件
with open('combined_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 'text_info' 和 'tables_info' 列表中的所有疾病信息
text_info = data.get('text_info', [])
tables_info = data.get('tables_info', [])


# 定义一个函数来清除 "第X节" 的字样
def remove_sections_and_lines(id_value):
    # 正则表达式匹配 "第X节" 模式，其中 X 是任意数字
    pattern = re.compile(r'第[^节]*节')
    # 使用正则表达式替换掉匹配的部分
    return pattern.sub('', id_value)

def remove_lines(text):
    # 正则表达式匹配 "第X节" 模式，其中 X 是任意数字
    # 并且匹配其后的整行内容
    pattern = re.compile(r'第[^节]*节.*?(?=\n|$)', re.DOTALL)
    # 使用正则表达式替换掉匹配的部分
    return pattern.sub('', text)

# 遍历 'text_info' 列表
for item in text_info:
    if 'id' in item:
        # 清除 'id' 中的 "第X节" 及其后整行内容并更新
        item['id'] = remove_sections_and_lines(item['id'])
    if '处理原则' in item:
        # 清除 '处理原则' 中的 "第X节" 及其后整行内容并更新
        item['处理原则'] = remove_lines(item['处理原则'])

# 遍历 'tables_info' 列表中的每个子列表
for sublist in tables_info:
    for item in sublist:
        if 'id' in item:
            # 清除 'id' 中的 "第X节" 及其后整行内容并更新
            item['id'] = remove_sections_and_lines(item['id'])
        if '处理原则' in item:
            # 清除 '处理原则' 中的 "第X节" 及其后整行内容并更新
            item['处理原则'] = remove_lines(item['处理原则'])



# 将 'text_info' 和 'tables_info' 中的每个元素转换成 JSON 字符串，并格式化
cleaned_text_info = ',\n'.join(f"    {json.dumps(item, ensure_ascii=False, indent=4)}" for item in text_info)
cleaned_tables_info = ',\n'.join(f"    {json.dumps(item, ensure_ascii=False, indent=4)}" for sublist in tables_info for item in sublist)

# 将清理后的数据合并到一个字符串中，每个 JSON 对象之间用逗号分隔
cleaned_data = f"[\n{cleaned_text_info},\n{cleaned_tables_info}\n]"


# 将合并后的字符串写入新的 JSON 文件
with open('cleaned1_data.json', 'w', encoding='utf-8') as f:
    f.write(cleaned_data)

print('数据清理完成，结果已保存到 cleaned1_data.json 文件。')