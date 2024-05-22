# app.py
from flask import Flask, request, render_template, jsonify
from bm25_service import read_diseases_json, bm25, search_disease
from search_by_symptom import search_by_symptom

app = Flask(__name__)

# 全局变量
diseases = None
avgdl = None
idf = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global diseases, avgdl, idf
    if diseases is None or avgdl is None or idf is None:
        diseases, avgdl, idf = read_diseases_json('cleaned3_data.json')
    
    symptom = request.form.get('symptom', '').strip()
    search_method = request.form.get('search_method', 'bm25')
    best_diseases = []
    
    if request.method == 'POST':
        if symptom.lower() == 'exit':
            return '退出程序。'
        if search_method == 'bm25':
            best_diseases = search_disease(symptom, diseases, avgdl, idf, top_n=2)
        elif search_method == 'string_match':
            best_diseases = search_by_symptom(diseases, symptom)
        else:
            return jsonify({'error': '无效的搜索方法'}), 400
    
    return render_template('index.html', best_diseases=best_diseases, symptom=symptom, search_method=search_method)

if __name__ == '__main__':
    app.run(debug=True)