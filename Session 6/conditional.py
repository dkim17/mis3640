# age = input('please enter your age: ')

# if int(age) >= 18:
#     print('adult')
# elif: int(age) >= 6 :
#     print('teenager')
# else:
#     print('kid')


# if x == y:
#     print('x and y are equal')
# else:
#     if x<y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')

# def calculate_bmi(weight, height):
#     bmi = 703 * weight/(height * height)

# if bmi <= 18.5:
#     print("your bmi is {:.lf). You are underweighted.".format(bmi))
# elif 18.5 < bmi <= 25:
#     print('normal weight')
# elif  25< bmi <= 29.9:
#     print('overweight')
# elif bmi > 30:
#     print("obesity")

# print(calculate_bmi(78, 180))

def compare(varA, varB):
    if insistance(varA, str) or isinstance(varB, str):
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA == varB:
            print('equal')
        else:
            print('smaller')

a = 'hello'
b = 3
c = 5

compare(a,b)
compare(b,c)

def countdown(n):
    if n <=0:
        return
    print(s)
    print_n(s, n-1) 