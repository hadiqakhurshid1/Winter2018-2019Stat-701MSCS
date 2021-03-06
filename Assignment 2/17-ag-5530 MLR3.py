from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as an
from statsmodels.stats.anova import anova_lm



a = pd.DataFrame({"Router": [10,10,20,20,50,70,80,90,99], "Switches": [100,200,300,400,500,600,700,800,900], "Network": [5,7,11,17,19,11,17,19,20]})
result = an.ols(formula="Network ~ Router + Switches", data=a).fit()
print result.params
print(anova_lm(result))
print(result.summary())

fig = plt.figure()
axis = fig.add_subplot(111, projection='3d')
axis.scatter(a['Router'], a['Switches'], a['Network'], c='r', marker='o')
xx, yy = np.meshgrid(a['Router'],a['Switches'])
exog = pd.core.frame.DataFrame({'Router':xx.ravel(),'Switches':yy.ravel()})
out = result.predict(exog=exog)
axis.plot_surface(xx, yy, out.values.reshape(xx.shape), rstride=1, cstride=1, alpha='0.2', color='None')
axis.set_xlabel("Router")
axis.set_ylabel("Switches")
axis.set_zlabel("Network")
plt.show()

