# print(42 * 60 +42)
# print(10/1.61)
# print((10/1.61)/(42+42/60))
# print((10/1.61)/(42 * 60 +42))
# print((10/1.61)/(42/60+42/360))


#September 4th
#1. 
pi = 3.141592653589793
r =5
v = 4.0/3.0*pi*r**3
print('The volume of sphere is', v)

#2. 
cover_price = 24.95
total_cost = cover_price * 60 *.6
print(total_cost)
shipping_cost= 3 + (.75 * 59)
print(shipping_cost)
print('Total cost is {:0.2f}'.format(total_cost + shipping_cost))

#3.
easy_pace = 8.25 * 2
tempo = 7.2 *3
total_time = easy_pace + tempo
print(total_time)
#He eats breakfast 38:06 later, so breakfast time will be 7:30 in the morning.


#4. 
difference = 89-82
percent_increase = difference/82*100
print('Percent increase is {:.2f}%'.format(percent_increase))

#Quadratic
def quadratic(a, b, c):
    a= type(int())
    b= type(int())
    c= type(int())
    root = quadratic(b**b-4*a*c)

print(quadratic)