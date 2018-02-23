##########################################################
# Delete data that appears more than n times in a list   #
# Inputs:                                                #
#   data: the list to be altered                         #
#   n: the number of times an element is allowed in data #
# Output:                                                #
#   the altered list                                     #
##########################################################

def remove(data, n):
    # checks
    if n >= len(data): # no task will appear more than n times
        return data
    if len(data) == 0: # empty list
        return data
    if n == 0: # no task will remain
        del data[:]
        return data

    # keep track of how many times a shift appears
    count = {}
    for task in data:
        if task not in count:
            count[task] = 1;
        else:
            count[task] += 1;

    # iterate and filter out values > n
    for num in count:
       if count[num] > n:
           data = list(filter(lambda x: x != num, data))

    return data
