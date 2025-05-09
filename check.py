#만점 20점인 출석 점수에서 특정 기준에 따라 점수를 산정하는 프로그램

#출석 점수 함수
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    
    total_absence_hour = absence_hours+(tardy_count//3)
    
    if total_absence_hour > (hours_per_week*15)/4:
            return f"당신의 출석 점수는 F (학점 미부여)점 입니다."
    else:
        attendance_score = 20 - (20*(total_absence_hour)/(hours_per_week*15))
    
    attendance_score = round(attendance_score,2)
    return f"당신의 출석 점수는 {attendance_score}점 입니다."


#주당 수업시간, 결석시간, 지각횟수를 입력 받는다.
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

#함수 호출 및 결과 출력
print(calculate_attendance_score(hours_per_week,absence_hours,tardy_count))