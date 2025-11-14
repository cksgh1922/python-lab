import numpy as np
import matplotlib.pyplot as plt

class Quadratic:
    """이차함수 ax^2 + bx + c 를 다루는 클래스"""
    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            raise ValueError("a는 0일 수 없습니다 (이차함수가 아닙니다).")
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        """근을 반환 (실수 또는 복소수)"""
        coeffs = [self.a, self.b, self.c]
        r = np.roots(coeffs)
        # 실수에 가까운 값은 실수형으로 변환
        r_real = [float(x.real) if abs(x.imag) < 1e-9 else complex(x) for x in r]
        return tuple(r_real)

    def vertex(self):
        """꼭짓점 좌표 (x, y)를 반환"""
        x_v = -self.b / (2 * self.a)
        y_v = self.a * x_v**2 + self.b * x_v + self.c
        return (x_v, y_v)

    def y(self, x):
        """주어진 x에 대한 y값 계산 (스칼라 또는 numpy 배열 허용)"""
        return self.a * x**2 + self.b * x + self.c

    def plot(self, x_min=None, x_max=None, num=400, show=True, annotate=True):
        """그래프를 그립니다.
        - x_min/x_max가 지정되지 않으면 근과 꼭짓점을 기반으로 범위를 자동 설정합니다.
        - annotate=True이면 근과 꼭짓점을 표시하고 라벨을 붙입니다.
        """
        # 자동 x 범위 설정
        r = self.roots()
        xv, yv = self.vertex()

        if x_min is None or x_max is None:
            xs = [xv]
            for val in r:  # 실수근만 범위 계산에 사용
                if isinstance(val, complex):
                    continue
                xs.append(val)
            x_center = np.mean(xs)
            span = max(1.0, max(abs(x - x_center) for x in xs) * 2.5)
            x_min = x_center - span
            x_max = x_center + span

        x = np.linspace(x_min, x_max, num)
        y = self.y(x)

        plt.figure(figsize=(8,6))
        plt.plot(x, y, label=f"y={self.a}x² + {self.b}x + {self.c}")

        if annotate:
            # 근 표시 (실수인 경우만)
            roots = self.roots()
            for i, rt in enumerate(roots):
                if isinstance(rt, complex):
                    continue
                plt.scatter([rt], [0], zorder=5)
                plt.text(rt, 0, f"  root{ i+1 }={rt:.2f}", verticalalignment='bottom', fontsize=9)

            # 꼭짓점 표시
            plt.scatter([xv], [yv], s=80, marker='^', zorder=6)
            plt.text(xv, yv, f"  vertex=({xv:.2f}, {yv:.2f})", verticalalignment='bottom', fontsize=10)

        plt.axhline(0)
        plt.axvline(0)
        plt.xlabel("x (초)")
        plt.ylabel("y (높이, m)")
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.legend()
        if show:
            plt.show()

# 예시: y = -5x^2 + 20x
q = Quadratic(-2, 12, -10)
print("Roots:", q.roots())
print("Vertex:", q.vertex())

# 그래프 출력
q.plot()
