
def roman_integer(string):
    romandict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    numlist = []
    for i in range(0, len(string)):
        character = string[i]
        x = romandict.get(character)
        numlist.append(x)
    for i in range(0, len(numlist)):
        if (numlist[i] < numlist[i+1]):
            numlist[i] = numlist[i+1]

def main():
    romanString = 'IIVL'
    retval = roman_integer(romanString)
    print(retval)
main()