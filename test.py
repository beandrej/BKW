import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 8760, 1)
y1 = pd.read_csv(r"ren_ninja/ESP/T2M_2019_MAD.csv", delimiter=",", header=3)["t2m"].tolist()
y2 = pd.read_csv(r"ren_ninja/ESP/T2M_2019_BAR.csv", delimiter=",", header=3)["t2m"].tolist()

print(np.mean(y1))
print(np.mean(y2))

plt.plot(x, y1, label='MAD')
plt.plot(x, y2, label='BAR')
plt.legend()
plt.show()