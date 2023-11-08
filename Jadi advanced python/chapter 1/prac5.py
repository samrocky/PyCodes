#a = 'The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.'
import re
import string
a = input()

def find_capital_words(text):
    texts = text.strip()
    texts = texts.split('.')
    for i in range(len(texts)):
        texts[i] = texts[i].strip()
        texts[i] = texts[i].split()
    words = []
    for tex in texts[0:-1]:
        tex[0] = 'a'
        words = words + tex
    #print(words)

    for i, word in enumerate(words, 1):
        if re.match(r"^[A-Z]", word):
            print(f"{i}:{word.strip(string.punctuation)}")
    if not any(re.match(r"^[A-Z]", word) for word in words):
        print("None")

find_capital_words(a)
