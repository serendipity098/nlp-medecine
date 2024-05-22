import json
import jieba
from math import log
from tqdm import tqdm
from collections import Counter

# 读取JSON文件中的疾病数据，并计算idf和df
def read_diseases_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # 计算文档频率和逆文档频率
    df = Counter()
    for d in data:
        words = set(jieba.cut_for_search(d.get('临床表现', '')))
        df.update(words)
    
    idf = {word: log(len(data) / (df[word] + 1)) for word in df}
    
    # 计算所有文档的平均长度
    avgdl = sum(len(jieba.lcut(d.get('临床表现', ''))) for d in data) / len(data)
    
    return data, avgdl, idf

# BM25算法函数
def bm25(query, document, idf, k1=1.0, b=0.75, avgdl=0):
    if not document:  # 检查文档内容是否为空
        return 0

    query_words = set(jieba.cut_for_search(query))
    document_words_count = Counter(jieba.cut_for_search(document))
    
    score = 0.0
    for word in query_words:
        if word in idf:
            tf = document_words_count[word]
            score += (tf * (k1 + 1) * idf[word]) / (tf + k1 * (1 - b + b * len(document_words_count) / avgdl))
    
    return score

# 主函数
def main():
    global diseases, avgdl, idf
    # 从JSON文件中读取疾病数据，并计算idf和df
    diseases, avgdl, idf = read_diseases_json('cleaned3_data.json')
    
    while True:
        # 用户输入提示词
        prompt_words = input("请输入提示词（输入'exit'退出）：").strip()
        if prompt_words.lower() == 'exit':
            break
        
        # 初始化最佳匹配的分数和内容
        best_score = 0
        best_disease = None
        
        # 使用tqdm显示进度
        for disease in tqdm(diseases, desc='Processing', total=len(diseases)):
            # 计算当前疾病的BM25分数
            score = bm25(prompt_words, disease.get('临床表现', ''), idf, avgdl=avgdl)
            # 如果当前分数高于最佳分数，则更新最佳分数和最佳疾病内容
            if score > best_score:
                best_score = score
                best_disease = disease
        
        # 如果找到最佳匹配，则打印出来
        if best_disease:
            print("最相关的疾病内容：")
            for key, value in best_disease.items():
                print(f"{key}: {value}")
        else:
            print("没有找到相关的疾病信息。")

# 运行主函数
if __name__ == "__main__":
    main()