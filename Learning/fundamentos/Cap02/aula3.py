import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns

#%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sns.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

plt.bar(x, y)

plt.show()