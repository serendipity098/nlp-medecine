import json
from collections import Counter

# 读取JSON数据
with open('cleaned2_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取关键信息
id_clinical_appearances = [(d['id'], d['临床表现'].replace(' ', '')) for d in data if 'id' in d and '临床表现' in d]

# 计算id内容相同的组数
id_counts = Counter([id_ for id_, _ in id_clinical_appearances])
id_duplicates_count = sum(count for count in id_counts.values() if count >= 2)

# 计算id和临床表现内容都相同的组数
id_clinical_appearances_counts = Counter(id_clinical_appearances)
id_clinical_appearances_duplicates_count = sum(count for count in id_clinical_appearances_counts.values() if count >= 2)

print("具有相同ID的组数（出现至少两次）：", id_duplicates_count/2)
print("具有相同ID和临床表现内容的组数（出现至少两次）：", id_clinical_appearances_duplicates_count/2)
import json
from collections import Counter


# 提取关键信息
id_clinical_appearances = [(d['id'], d['临床表现'].replace(' ', '')) for d in data if 'id' in d and '临床表现' in d]

# 计算id内容相同的组数并输出重复的id名称
id_counts = Counter([id_ for id_, _ in id_clinical_appearances])
id_duplicates = [id_ for id_, count in id_counts.items() if count >= 2]

print("重复的id名称：", id_duplicates)

# 计算id和临床表现内容都相同的组数
id_clinical_appearances_counts = Counter(id_clinical_appearances)
id_clinical_appearances_duplicates_count = sum(count for count in id_clinical_appearances_counts.values() if count >= 2)

print("具有相同ID和临床表现内容的组数（出现至少两次）：", id_clinical_appearances_duplicates_count)
