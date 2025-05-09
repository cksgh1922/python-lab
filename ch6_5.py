score = [99,29,30,40,20,60]

sum = 0
for list in score:
    sum += list


print(f"학생 수 : {len(score)}, 총점 : {sum}, 평균 : {sum/len(score)}")