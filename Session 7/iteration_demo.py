# result = 0 

# for i in range(1,1001):
#     print('current number to be added:', i)
#     result = result + i 
#     print('new result after this iteration:', result)

# print('The final result:', result)

#2
# result = 0 

# for i in range(1,1001):
#     if i%2 == 0:
#        result = result + i

# print('The sum of odd numbers is', result)

# result = 0 

# for i in range(1, 1001, 2):
#        result = result + i

# print('The sum of odd numbers is', result)

#factorial
# result = 1

# for i in range(1, 11): 
#     result = result * i

# print('The factorial of 10 is', result)

# #while statement
# import time

# def countdown(n):
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n = n - 1
#     print('BlastOff')

# countdown(5)


while True: #keep going until happen
    print('press "q" to quit')
    line = input('> ')
    if line == 'q':
        break
    print(line)

print('Done!')