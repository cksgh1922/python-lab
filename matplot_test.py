import matplotlib.pyplot as plt
from matplotlib import rc


x = [val for val in range(0,21)]
y = [val*2 for val in x]

print(x)
print(y)

#Graph
plt.scatter(x,y, color='red',marker="*") #산점도도 graph

#Graph Visualization
plt.xlabel("X Line")
plt.ylabel("Y Line")
plt.title("Graph")
plt.grid(True)

#Graph print
plt.show()