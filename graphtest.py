import matplotlib.pyplot as plt
import numpy as np

# 1. x 값의 범위 설정
# -10부터 10까지 100개의 점을 생성하여 부드러운 곡선을 만듭니다.
x = np.linspace(-10, 6, 100)

# 2. y 값 계산 (y = x^2 + 8x + 12)
y = x**2 + 4*x + 3

# 3. 그래프 그리기
plt.figure(figsize=(8, 6)) # 그래프 크기 설정 (선택 사항)
plt.plot(x, y) # 그래프 선 그리기

# 4. 그래프 꾸미기
plt.title('Graph of $y = x^2 + 8x + 12$') # 그래프 제목
plt.xlabel('X-axis') # X축 라벨
plt.ylabel('Y-axis') # Y축 라벨
plt.axhline(y=0, color='k') # X축을
plt.axvline(x=0, color='k') # Y축을
plt.legend() # 범례 표시

# 5. 그래프 보여주기
plt.show()