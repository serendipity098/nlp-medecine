# nlp-medecine
运行步骤：

1.运行combine.py将book.docx中的常规结构病情和表格结构病情提取出来，保存到combined_data.json文件中。

2.运行json_clean1.py将combined.py文件中两种类型的json合并，同时去除处理原则中和id中含有第**节字样的部分，保存至cleaned1_data.json文件中。
    
3.运行json-clean2.py将cleaned1_data.json文件中处理原则中含有的下一个疾病的id的共同内容去除，保存最后清理的内容至cleaned2_data.json文件中。
    
4.运行json-clean3.py将json-clean2.json中重复的疾病名称去除内容,保存至cleaned3_data.json文件中。
    
5.运行app.py进行web运行，通过生成的网址进行疾病查询。
end
