# myString = " It is a great weather with you"
# count = 0
# word = ""
# for char in myString:
#     if char != " " :
#         word += char
#     elif char == " " and word != "":
#         count += 1
#         word = ""

# if word != "":
#     count +=1

# print("문자열 단어 갯수 : ", count)

# #다시해보기

# 문자열이 아닌 리스트로 한글자씩 추가해서 합치는 느낌.
'''
myString = "  "
count = 0
sentence = []
for char in myString:
    if char != " " :
        sentence += char
        print(sentence)
    elif char == " " and sentence:
        count+=1
        sentence = []
if sentence:
    count += 1
print("문자열 단어 갯수 : ", count)

'''