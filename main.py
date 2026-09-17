import sys

from src.classifier import load_keywords, classify, translate

loaded_keywords = load_keywords('data/keywords.txt')
translated_words = translate('data/translate.txt')

if len(sys.argv) > 1:
    label, score = classify(sys.argv[1],loaded_keywords)
    print(f"해당 문장은 {translated_words[label]}적인 내용입니다.")
else:
    print("quit 입력시 종료")
    while True:
        comment = input()
        if comment == 'quit':
            break
        label, score = classify(comment, loaded_keywords)
        print(f"해당 문장은 {translated_words[label]}적인 내용입니다.")
