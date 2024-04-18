# doc = open('read.txt', 'rt', encoding='utf-8')
# for i in doc:
#     print (i)

with open('read.pdf', 'wt', encoding='utf-8') as file:
    doc=open('read.txt', 'rt', encoding='utf-8')
    for i in doc:
        file.write(i)
