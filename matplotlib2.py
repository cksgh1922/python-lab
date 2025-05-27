import matplotlib.pyplot as plt

x = range(-10,11)
y1 = [2*val for val in x]
y2 = [4*val for val in x]
y3 = [8*val for val in x]

plt.plot(x,y1,label="y1",color="blue",marker='o')
plt.plot(x,y2,label="y2",color="red",marker='x')
plt.plot(x,y3,label="y2",color="green",marker='*')

plt.legend()
plt.title("X Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()