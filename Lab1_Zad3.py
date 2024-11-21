
import re
import os

# postal code regex:    ([0-9]{2}-[0-9]{3})

def delexp(text, word):
    return re.sub(word, "", text)

def switchexp(text, change, into):
    return re.sub(change, into, text)

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__, "Lab1_Zad3_Text.txt"))
text_in = file.read()
count_in_lorem = len(re.findall("lorem", text_in))
count_in_ipsum = len(re.findall("ipsum", text_in))

text_del = delexp(file.read(), "Napisz")
count_del = len(re.findall("lorem", text_del))

text_switch = switchexp(text_in, "lorem", "ipsum")
count_lorem = len(re.findall("lorem", text_switch))
count_ipsum = len(re.findall("ipsum", text_switch))

print(f"Number of \"lorem\" in input: {count_in_lorem}") 
print(f"Number of \"ipsum\" in input: {count_in_ipsum}") 
print(f"Number of \"lorem\" after delexp: {count_del}") 
print(f"Number of \"lorem\" after switchexp: {count_lorem}") 
print(f"Number of \"ipsum\" after switchexp: {count_ipsum}") 
