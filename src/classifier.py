import re

def load_keywords(path: str):
    result = {}
    with open(path, 'r', encoding='UTF-8') as f:
        content = f.read()
    content = content.split('\n')

    for i in content:
        batch = re.split(':|,',i)
        if batch[0] != '':
            result.update({batch[0]:[b.strip() for b in batch[1:]]})

    return result

def classify(text: str, keywords: dict):
    count_dict = {}
    for key, value in keywords.items():
        num = 0
        for word in value:
            num += text.count(word)
        count_dict.update({key:num})

    max_count = max(count_dict.values())
    arr = [k for k,v in count_dict.items() if max_count == v]
    if len(arr) > 1:
        return 'neutral', 0
    else:
        return arr[0], count_dict[arr[0]]

def translate(path: str):
    with open(path, encoding='UTF-8') as f:
        content = f.read()
    content = content.split('\n')
    translate_dict = {}
    for word in content:
        key, value = word.split(':')
        if key != '':
            translate_dict.update({key.strip():value.strip()})
    return translate_dict