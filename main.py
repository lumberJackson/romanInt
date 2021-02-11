# convert a roman integer into a number
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

    # must find out if it is ascending, descending, or equal
    if (numlist[len(numlist)-1] > numlist[0]):
        #ascending
        reversedList = numlist[::-1]
        for i in range(1, len(numlist)):
            numlist[0] = numlist[0] - numlist[i]
    if (numlist[len(numlist)-1] < numlist[0]):
        #descending

    if(numlist[len(numlist)-1] == numlist[0]):
        #just sum up the list (equal)

    retval = numlist[0]
    return retval



def main():
    romanString = 'IIV'
    retval = roman_integer(romanString)
    print(retval)
main()