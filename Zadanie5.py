from collections import Counter
def purified(text):
    return "".join(text.split()).lower()
f = open("text.txt")
text = f.read()
print(Counter(purified(text)))