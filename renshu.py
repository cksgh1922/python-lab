word_list = []

for i in range(5):
    word_list.append(list(input()))

new_word = ""
for i in range(15):
    for j in range(15):
        try:
            new_word += word_list[j][i]
        except:
            continue
print(new_word)