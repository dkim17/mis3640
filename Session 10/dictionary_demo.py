names = ['Defne', 'Jack', 'Angela']
scores = [95, 75, 85]

grades = dict()
print(grades)

grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
print(grades)

print(grades['Jack'])    

print(len(grades))

'Jack' in grades

90 in grades.values()

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)

number_of_e = h.get('e', 0)
number_of_a = h.get('a', 0)
print(number_of_e)
print(number_of_a)

#Exercise 1
# def histogram(s):
#     d = dict()
#     for c in s:
#         d.get(c, 0)

def print_hist(h):
    for letter not in d:
        d[letter] = 1
    else: 
        d[letter] += 1
    
        
h = histogram('Massachusetts')
print_hist(h)


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)

inverse = invert_dict(hist)
print(inverse)

#exercise 2
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)

#exercise 3
#config, mod, lambada...

#exercise 4
fin = open('Session 9/words.txt')

def create_word_dict():
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word] = word
    return word_dict

def has_duplicates(s):
    for line in fin:
        word = line.strip()
        if s.count(i) > 1:
            return True
    return False



numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

t = [1, 2, 3]
print(sum(t))

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

