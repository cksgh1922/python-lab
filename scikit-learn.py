import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#csv파일을 데이터로드
#feature개수는 두개, 분출시간, 다음분출까지 대기시간
#-skiprows=1 : 첫 줄은 헤더 (설명) 이므로 건너뜀
#delimiter="," ,기준으로 나눔
data = np.loadtxt("old_faithful_geyser.csv", delimiter=",",skiprows = 1)

#열 0: 분출시간, 열 1: 다음 분출까지의 대기 시간
X = data

#Kmeans 클러스터링 수행(Clustering 개수 2개)
#random_state : 결과재현성을 위한 시드값 고정 S
kmeans = KMeans(n_clusters=2,random_state=0)
kmeans.fit(X)

#클러스터 레이블 및 중심점 추출
labels = kmeans.labels_ #각 샘플이 속한 클러스터 번호(0 또는 1)

centroids = kmeans.cluster_centers_ #각 클러스터의 중심 좌표

#cost function (SSE: sum of squared errors) 출력
# inertia_: 각 점과 해당 클러스터 중심점 간 거리 제곱의 총합
print(f"SSE : {kmeans.inertia_:.2f}")

#결과 시각화
plt.figure(figsize=(8,6))

# 데이터 포인트 산점도 (색상은 클러스터 레이블에 따라 지정)
plt.scatter(X[:,0],X[:,1],c=labels,s=80,cmap='Accent',label='Point')
# 클러스터 중심점 표시 (빨간색 X 마커)
plt.scatter(centroids[:,0],centroids[:,1],c='red',marker="X",s=200,label='Centroids')

#그래프 정보 설정
plt.xlabel("Eruption duration (min)")
plt.ylabel("Waiting time (min)")
plt.title("K-means Clustering (NumPy oonly, no pandas)")
plt.legend()
plt.grid(True)
plt.show()

#17 - 21 라인 해석 후 보고서 작성