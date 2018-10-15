import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

x=np.array([10,10,20,20,50,70,80,90,99])
y=np.array([100,200,300,400,500,600,700,800,900])
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=-1)[0]
print(m, c)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.ylabel("Switches")
plt.xlabel("Router")
plt.title("Making a Regression Line")
plt.legend()
plt.show()