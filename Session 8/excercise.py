#3
'   spacious   '.rstrip()
'   spacious'
'mississippi'.rstrip('ipz')
'mississ'




#4
item = ["bananas", "rice", "paprika", "potato chips"]

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

print(values["a"])

pbananas = values["b"] + values["a"] + values["n"] + values["a"] +values["n"] + values["a"] + values["s"]
pprice = values["r"] + values["i"] + values["c"] + values["e"]
ppaprika = values["p"] + values["a"] + values["p"] + values["r"] + values["i"] + values["k"] + values["a"]
ppotatochips = values["p"] + values["o"] + values["t"] + values["a"] + values["t"] + values["o"] + values["c"] + values["h"] + values["i"] + values["p"] + values["s"]

price = [pbananas, pprice, ppaprika, ppotatochips]

def receipt:
    print('{:3} {:14}'.format('item', 'price'))
    print('{:3} {:14}'.format('-', '---------'))



