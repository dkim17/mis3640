# import os
# print(os.getcwd())

# fout = open('Session 14/output.txt', 'a')

# line1  = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath('Session 14/output.txt', 'a'))




# a = [1,2,3]
# try:
#     print(a[1.5])
# except:
#     print('Something is wrong.')

# folder = os.getcwd()

# walk(folder)

import pickle

t1 = [1,2,3]

f = open('save.p', 'wb')
s = pickle.dump(t1, f)
f.close()