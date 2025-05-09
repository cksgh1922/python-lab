# 각 학기별 최고의 점수 찾기

score = [89,19,30,40,50,86,40,30,21,80]

first_semester = score[0:(len(score)//2)]
second_semester = score[(len(score)//2):-1]

print(f"1학기 최고 점수: {max(first_semester)}")
print(f"2학기 최고 점수: {max(second_semester)}")