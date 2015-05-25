import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("stat_new.csv", sep=";")

plt.plot(np.arange(47), df.sort("best_size")["best_size"].values, 'ro')

#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 48, 0, 500])
plt.show()



plt.plot(np.arange(47), df.sort("len_sequences")["len_sequences"].values, 'ro')

plt.axis([0, 48, 0, 1500], 'ro')
plt.show()


plt.plot(np.arange(47), df.sort("time")["time"].values, 'ro')

plt.axis([0, 48, 0, 250], 'ro')
plt.show()

time_positive = df[df['filename'].str.contains("\+")].sort("time")["time"]
plt.plot(np.arange(len(time_positive)), time_positive.values, 'ro')
plt.show()

time_negative = df[df['filename'].str.contains("\-")].sort("time")["time"]
plt.plot(np.arange(len(time_negative)), time_negative.values, 'ro')
plt.show()



#plt.plot(np.arange(47), df[df['filename'].str.contains("\-")].sort("time")["time"].values, 'ro')

