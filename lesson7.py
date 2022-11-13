import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

axes = plt.subplots(2, 1)

data = pd.Series(np.random.randn(5).cumsum(), index=np.arange(0, 50, 10))
data.plot(ax=axes[1][0], kind="bar", color="black")

data = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
data.plot(ax=axes[1][1], title="Ломаная", style="--", alpha=0.7, kind="line", color="red", figsize=(20, 30))

plt.show()

