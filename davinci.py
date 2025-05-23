#입력받기
sentence = input("문자와 숫자가 섞인 문자열을 입력하세요 : ")

#리스트 선언
num_list = []
davinci_list = []

#숫자만 isdigit을 활용하여 추출하고, int()해서 바꿔서 list에 집어넣기
for val in sentence:
    if val.isdigit():
        num_list.append(int(val))  
        #리스트 반복문으로 , if문으로 홀수 짝수 구분하여 -1, 1 저장
        if int(val) % 2:
            davinci_list.append(-1)
        else:
            davinci_list.append(1)

subarray_list = []
#인덱스 범위 0부터 리스트 길이만큼 비교하며, 리스트 길이 -1씩 줄어드는 중복 반복문
for i in range(len(num_list),0,-1):
    for j in range(len(num_list)):
        if sum(davinci_list[j:i]) == 0:
            if davinci_list[j:i] != []:
                subarray_list.append(davinci_list[j:i])

#입력문자열,숫자추출,변환리스트출력
print(f"""
입력 문자열 : {sentence}
숫자 추출 : {num_list}
변환된 리스트 (+1/-1): {davinci_list}
합이 0인 연속 부분 수열 목록 :""")
#합이 0인 연속 부분 수열 목록
for item in subarray_list:
    print(f"- {item}")