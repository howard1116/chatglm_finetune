import os
import json

Instruction = '''你现在是一个很厉害的阅读理解器，严格按照人类指令进行回答。'''
Input = '''从下面的论文片段中提取三元组信息，以json格式输出。三元组应当包括信息的主语"subject"；信息的谓语"predicate"；信息的宾语"object"'''
Paragraph = '''环氧树脂（EP）具有高模量、耐水性和耐溶剂性良好等特点，且分子结构中含有可与异氰酸酯基团（—NCO）反应的仲羟基以及环氧基团，另外环氧基团自身可开环交联。'''
Target = '''```json
[{"subject":"环氧树脂",
"predicate":"特点",
"object":{"高模量","耐水性","耐溶剂性良好"}},

{"subject":"环氧树脂",
"predicate":"分子结构",
"object":{"仲羟基","环氧基团"}}

{"subject":"仲羟基",
"predicate":"可反应对象",
"object":"异氰酸酯基团（—NCO）"},

{"subject":"环氧基团",
"predicate":"特点",
"object":"自身可开环交联"}]
```'''

def get_instance(Paragraph, Target):
    Context = f'''Instruction: {Instruction}
    Input: {Input}

    {Paragraph}
    Answer: '''
    return {"context": Context, "target": Target}

with open('eval_dataset.jsonl', 'w') as output_file:
    output_file.write(json.dumps(get_instance(Paragraph, Target), ensure_ascii = False) + '\n')

with open('train_dataset.jsonl', 'w') as output_file:
    for idx in range(10):
        with open(os.path.join('select', f'Paragraph_{idx}.txt'), 'r') as input_file:
            Paragraph = input_file.readline()
        with open(os.path.join('select', f'Target_{idx}.txt'), 'r') as input_file:
            Target = '\n'.join(input_file.readlines())
        output_file.write(json.dumps(get_instance(Paragraph, Target), ensure_ascii = False) + '\n')