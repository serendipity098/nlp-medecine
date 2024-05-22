#bm25_service.py
import json
import jieba
from math import log
from collections import Counter

def read_diseases_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    df = Counter()
    for d in data:
        words = set(jieba.cut_for_search(d.get('临床表现', '')))
        df.update(words)
    
    idf = {word: log(len(data) / (df[word] + 1)) for word in df}
    
    avgdl = sum(len(jieba.lcut(d.get('临床表现', ''))) for d in data) / len(data)
    
    return data, avgdl, idf

def bm25(query, document, idf, avgdl):
    if not document:  
        return 0

    query_words = set(jieba.cut_for_search(query))
    document_words_count = Counter(jieba.cut_for_search(document))
    
    score = 0.0
    k1 = 1.0
    b = 0.75
    for word in query_words:
        if word in idf:
            tf = document_words_count[word]
            score += (tf * (k1 + 1) * idf[word]) / (tf + k1 * (1 - b + b * len(document_words_count) / avgdl))
    
    return score

def search_disease(query, diseases, avgdl, idf, top_n=2):
    scores = [(bm25(query, disease.get('临床表现', ''), idf, avgdl), disease) for disease in diseases]
    scores.sort(key=lambda x: x[0], reverse=True)
    return [(score, disease) for score, disease in scores[:top_n]]
