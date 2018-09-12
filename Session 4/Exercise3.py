# Exercise 3

import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
print('Current time: {:d} days, {:d} hours, {:d} minutes and {:.2f} seconds from Epoch.' .format(
        int})