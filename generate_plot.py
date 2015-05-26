import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("stat_new.csv", sep=";")

# plt.plot(np.arange(47), df.sort("best_size")["best_size"].values, 'ro')

# #plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 48, 0, 500])
# #plt.show()



# plt.plot(np.arange(47), df.sort("len_sequences")["len_sequences"].values, 'ro')

# plt.axis([0, 48, 0, 1500], 'ro')
# #plt.show()


# plt.plot(np.arange(47), df.sort("time")["time"].values, 'ro')

# plt.axis([0, 48, 0, 250], 'ro')
# #plt.show()

# time_positive = df[df['filename'].str.contains("\+")].sort("time")["time"]
# plt.plot(np.arange(len(time_positive)), time_positive.values, 'ro')
# #plt.show()

# time_negative = df[df['filename'].str.contains("\-")].sort("time")["time"]
# plt.plot(np.arange(len(time_negative)), time_negative.values, 'ro')
# #plt.show()


negative_random = df[df['filename'].str.contains('9.200-40|9.200-80|18.200-40|18.200-80|35.200-40|35.200-80|20.300-60|20.300-120|55.300-60|55.300-120|58.300-60|58.300-120|55.400-80|55.400-160|62.400-80|62.400-160|68.400-80|68.400-160|10.500-100|10.500-200|25.500-100|25.500-200|53.500-100|53.500-200')]

#print negative_random.sort("filename")

negative_repeat = df[df['filename'].str.contains('59\.500\-2|113\.500\-8|144\.500\-12|28\.500\-18|34\.500\-32')]

positive_random = df[df['filename'].str.contains('9\.200\+80|18\.200\+80|35\.200\+80|20\.300\+120|55\.300\+120|58\.300\+120|55\.400\+160|62\.400\+160|68\.400\+160|10\.500\+200|25\.500\+200|53\.500\+200')]

positive_end_errors = df[df['filename'].str.contains('9\.200\+20|18\.200\+20|35\.200\+20|20\.300\+30|55\.300\+30|58\.300\+30|55\.400\+40|62\.400\+40|68\.400\+40|10\.500\+50|25\.500\+50|53\.500\+50')]

#plt.plot(np.arange(47), df[df['filename'].str.contains("\-")].sort("time")["time"].values, 'ro')

print len(negative_random)
print len(negative_repeat)
print len(positive_random)
print len(positive_end_errors)