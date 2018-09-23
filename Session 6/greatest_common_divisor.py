# def gcd(x,y):
#      if b > a:
#         if b % a == 0:
#             return a
#         else:
#             return gcd(b % a, a)
#     else:
#         if a % b == 0:
#             return b
#         else:
#             return gcd(b, a % b)  

# print(gcd(15, 5))

def gcdRecur(a,b):
    print('Current a,b:', a, b)
    if b==0:
        return a
    else: 
        return(b, a%b)

print(gcdRecur(12,9))