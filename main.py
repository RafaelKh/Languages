lang = input()
if lang == 'hy':
    f = open("hy.txt", 'r')
elif lang == 'ru':
    f = open("ru.txt", 'r')
elif lang == 'en':
    f = open("en.txt", 'r')
else:
    print('Something goes wrong')
print(f.read())
f.close()