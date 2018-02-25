##########################################################
# Sort versions in ascending order                       #
# Inputs:                                                #
#   l: list of unsorted versions                         #
# Output:                                                #
#   sorted list of strings in ascending order            #
##########################################################
def answer(l):
    for x in range(0, len(l)): # convert list to ints and separate by '.'
        l[x] = list(int(i) for i in l[x].split("."))
    l = insertionSort(l)
    for x in range (0, len(l)): # convert list to strings and join with '.'
        l[x] = ".".join(str(i) for i in l[x])
    return l

##########################################################
# Combines insertion sort and bucket sort to sort        #
# versions by major, minor, revision                     #
# Inputs:                                                #
#   l: list of unsorted versions                         #
# Output:                                                #
#   sorted list of ints in ascending order               #
##########################################################
def insertionSort(l):
    for version in range(2, -1, -1): # 0 = major, 1 = minor, 2 = revision
        for out in range(1, len(l)):
            try: # if IndexError, move element to front of list
                temp = l[out]
                tempNest = l[out][version]
            except IndexError:
                l.insert(0, l.pop(out))
                continue
            try: # if IndexError, continue to next iteration
                inn = out
                while inn > 0 and l[inn - 1][version] > tempNest:
                    l[inn] = l[inn - 1]
                    inn -= 1
                l[inn] = temp
            except IndexError:
                l[inn] = temp
    return l
