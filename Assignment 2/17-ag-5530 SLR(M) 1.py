import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

x=np.array([80,100,120,140,160,180,200,220,240,260])
y=np.array([70,65,90,95,110,115,120,140,155,150])
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=-1)[0]
print(m, c)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.ylabel("Expenditure")
plt.xlabel("Income")
plt.title("Making a Regression Line")
plt.legend()
plt.show()