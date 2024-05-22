#search_by_sympton
import re
def search_by_symptom(data, symptom):
    pattern = re.compile(re.escape(symptom), re.IGNORECASE)
    matched_records = []

    for record in data:
        if '临床表现' in record:
            matches = pattern.findall(record['临床表现'])
            if matches:
                record['match_count'] = len(matches)
                matched_records.append(record)

    matched_records.sort(key=lambda x: x['match_count'], reverse=True)
    
    # 构建包含分数和疾病信息的元组列表
    result = [(1.0, record) for record in matched_records]
    
    return result
