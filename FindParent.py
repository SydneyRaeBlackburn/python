##########################################################
# Find parent of node in a perfect binary tree that is   #
# in post order                                          #
# Inputs:                                                #
#   h: the height of the tree                            #
#   q: list of nodes whose parents need to be found      #
# Output:                                                #
#   list with parents, order maintained                  #
##########################################################
def answer(h, q):
    i = 0
    for node in q:
        if node == (2**h) - 1: # root node parent
            q[i] = -1
            i += 1
        else:
            q[i] = findParent(h - 1, (2**h) - 1, node)
            i += 1
    
    return q

##########################################################
# Recursive algorithm that eliminates half of the        #
# options with every recursive call                      #
# Inputs:                                                #
#   h: the height of the tree                            #
#   root: root of subtree                                #
#   num: node whose parent is to be found                #
# Output:                                                #
#   parent node                                          #
##########################################################
def findParent(h, root, num):
    left = root - (2**h)
    right = root - 1
    if num == left:
        return num + (2**h)
    if num == right:
        return num + 1
    if num > left:
        return findParent(h - 1, right, num) # search right subtree
    else:
        return findParent(h - 1, left, num) # search left subtree
