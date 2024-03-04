首先把运行目录移动到`my_data`文件夹下（）

然后，运行`select_data.py`，它会读取子文件夹`text`中的原始数据，输出节选片段到`select`子文件夹中

然后，需要根据`select/Paragraph_X.txt`人工标注`select/Target_X.txt`，`select_example`为一组标注样例

最后，运行`build_dataset.py`，生成`train_dataset.jsonl`与`eval_dataset.jsonl`