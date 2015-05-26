 # -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv("stat_new.csv", sep=";")

splits = df['filename'].str.split('.')
df['n'] = splits.str[1].str[:3]

# plt.plot(np.arange(47), df.sort("best_size")["best_size"].values, 'ro')

# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 48, 0, 500])
# plt.savefig('plots/1.png')



# plt.plot(np.arange(47), df.sort("len_sequences")["len_sequences"].values, 'ro')

# plt.axis([0, 48, 0, 1500], 'ro')
# #plt.show()


# plt.plot(np.arange(47), df.sort("time")["time"].values, 'ro')

# plt.axis([0, 48, 0, 250], 'ro')
# #plt.show()

# time_positive = df[df['filename'].str.contains("\+")].sort("time")["time"]
# plt.plot(np.arange(len(time_positive)), time_positive.values, 'ro')
# #plt.show()

#time_negative = df[df['filename'].str.contains("\-")].sort("time")["time"]
# plt.plot(np.arange(len(time_negative)), time_negative.values, 'ro')
# #plt.show()


negative_random = df[df['filename'].str.contains('9.200-40|9.200-80|18.200-40|18.200-80|35.200-40|35.200-80|20.300-60|20.300-120|55.300-60|55.300-120|58.300-60|58.300-120|55.400-80|55.400-160|62.400-80|62.400-160|68.400-80|68.400-160|10.500-100|10.500-200|25.500-100|25.500-200|53.500-100|53.500-200')]

#print negative_random.sort("filename")

negative_repeat = df[df['filename'].str.contains('59\.500\-2|113\.500\-8|144\.500\-12|28\.500\-18|34\.500\-32')]

positive_random = df[df['filename'].str.contains('9\.200\+80|18\.200\+80|35\.200\+80|20\.300\+120|55\.300\+120|58\.300\+120|55\.400\+160|62\.400\+160|68\.400\+160|10\.500\+200|25\.500\+200|53\.500\+200')]

positive_end_errors = df[df['filename'].str.contains('9\.200\+20|18\.200\+20|35\.200\+20|20\.300\+30|55\.300\+30|58\.300\+30|55\.400\+40|62\.400\+40|68\.400\+40|10\.500\+50|25\.500\+50|53\.500\+50')]

#plt.plot(np.arange(47), df[df['filename'].str.contains("\-")].sort("time")["time"].values, 'ro')
splits = negative_random['filename'].str.split('-')
negative_random['errors'] = splits.str[1]
splits = negative_repeat['filename'].str.split('-')
negative_repeat['errors'] = splits.str[1]

splits = positive_random['filename'].str.split('+')
positive_random['errors'] = splits.str[1]
splits = positive_end_errors['filename'].str.split('+')
positive_end_errors['errors'] = splits.str[1]

print len(negative_random)
print len(negative_repeat)
print len(positive_random)
print len(positive_end_errors)

print negative_random
print negative_repeat
print positive_random
print positive_end_errors

############################
# plt.plot(np.arange(len(negative_random)), df.sort("len_sequences")["len_sequences"].values, 'ro')
# plt.axis([0, 48, 0, 1500], 'ro')
# plt.savefig("plots/negative_random length")
#############################

#czas od ilosci bledow

plt.plot(negative_random.sort('errors')['errors'].values, negative_random.sort('errors')['time'].values, 'ro')
plt.axis([0, 250, 0, 50], 'ro')
plt.ylabel(u'czas przetwarzania')
plt.xlabel(u'ilość blędów negatywnych')
plt.savefig("plots/errors-time negative random")
plt.clf()

plt.plot(negative_repeat.sort('errors')['errors'].values, negative_repeat.sort('errors')['time'].values, 'ro')
plt.axis([0, 250, 0, 50], 'ro')
plt.ylabel(u'czas przetwarzania')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-time negative repeat")
plt.clf()

plt.plot(positive_random.sort('errors')['errors'].values, positive_random.sort('errors')['time'].values, 'ro')
plt.axis([0, 250, 0, 300], 'ro')
plt.ylabel(u'czas przetwarzania')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-time positive random")
plt.clf()

plt.plot(positive_end_errors.sort('errors')['errors'].values, positive_end_errors.sort('errors')['time'].values, 'ro')
plt.axis([0, 250, 0, 50], 'ro')
plt.ylabel(u'czas przetwarzania')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-time positive end errors")
plt.clf()

############################
# efektywnosc od ilosci bledow

plt.plot(negative_random.sort('errors')['errors'].values, negative_random.sort('errors')['efficiency'].values, 'ro')
plt.axis([0, 250, 0, 100], 'ro')
plt.ylabel(u'efektywność')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-efficiency negative random")
plt.clf()

plt.plot(negative_repeat.sort('errors')['errors'].values, negative_repeat.sort('errors')['efficiency'].values, 'ro')
plt.axis([0, 250, 0, 100], 'ro')
plt.ylabel(u'efektywność')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-efficiency negative repeat")
plt.clf()

plt.plot(positive_random.sort('errors')['errors'].values, positive_random.sort('errors')['efficiency'].values, 'ro')
plt.axis([0, 250, 0, 100], 'ro')
plt.ylabel(u'efektywność')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-efficiency positive random")
plt.clf()

plt.plot(positive_end_errors.sort('errors')['errors'].values, positive_end_errors.sort('errors')['efficiency'].values, 'ro')
plt.axis([0, 250, 0, 100], 'ro')
plt.ylabel(u'efektywność')
plt.xlabel(u'ilość błędów negatywnych')
plt.savefig("plots/errors-efficiency positive end errors")
plt.clf()




# czas od n

plt.plot(df.sort('n')['n'].values, df.sort('n')['time'].values, 'ro')
plt.axis([0, 550, 0, 700], 'ro')
plt.ylabel(u'czas przetwarzania')
plt.xlabel(u'n')
plt.savefig("plots/time - n")
plt.clf()


# efektywnosc od n

plt.plot(df.sort('n')['n'].values, df.sort('n')['efficiency'].values, 'ro')
plt.axis([0, 550, 0, 100], 'ro')
plt.ylabel(u'efektywność')
plt.xlabel(u'n')
plt.savefig("plots/efficiency - n")
plt.clf()


print negative_random["time"]
print negative_repeat["time"].mean
print positive_random["time"].mean
print positive_end_errors["time"].mean