import os
import random

data = []

for file_name in os.listdir('text'):
    with open(os.path.join('text', file_name), 'r') as f:
        s = ''.join(f.readlines()).replace('\n', '')
        while (len(s)):
            data.append(s[:150])
            if (len(s) <= 150):
                break
            s = s[50:]

print(len(data))
random.shuffle(data)

for idx, d in enumerate(data[:10]):
    if (os.path.isfile(os.path.join('select', f'Paragraph_{idx}.txt'))):
        continue
    with open(os.path.join('select', f'Paragraph_{idx}.txt'), 'w') as f:
        f.write(d)
    with open(os.path.join('select', f'Target_{idx}.txt'), 'w') as f:
        f.write('''```json
[{"subject":"",
"predicate":"",
"object":""},

{"subject":"",
"predicate":"",
"object":""},

{"subject":"",
"predicate":"",
"object":{"",""}},
]
```''')