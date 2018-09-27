# team = 'New England Patriots'
# letter = team[1]
# len(team)
# print(letter)

# print(team[0])

# print(team[1,5])

# team[1,0]

# 2**1000000000
# len(str(2**1000000000)

# team[20-1]
# team[-1]
# team[-20]

#Excercise 1
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

#String Slices

team = 'New England Patriots'

team[0:3]
team[0:11]
team[11:4]
team[::2]
team[::-2]

new_team = team[:12] + 'Beavers'
new_team
team

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'a'))

for i in range(len(team)):
    if team[i] == 'a':
        print(i)

for i, letter in enumerate(team):
    if letter == 'a':
        print(i, letter)

#excercise 2
team = 'New England Patriots'
def count(s, letter):
    c =0
    for each in s:
        if each == letter:
            c+1
    return c

            

print(count(team, 'a'))