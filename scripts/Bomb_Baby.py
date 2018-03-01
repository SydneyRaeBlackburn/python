##########################################################
# Replicate Mach and Facula bombc to destroy the         #
# LAMBCHOP doomsday device!                              #
# Inputs:                                                #
#   M: number of Mach bombs needed                       #
#   F: number of Facula bombc needed                     #
##########################################################
def answer(M, F):
    return str(BombBaby(int(M), int(F), 0))

##########################################################
# find the number of replication cycles needed to        #
# generate the correct amount of bomb                    #
# Inputs:                                                #
#   M: number of Mach bombs needed                       #
#   F: number of Facula bombc needed                     #
#   gen: number of replication cycles                    #
##########################################################
def BombBaby(M, F, gen):
    if M == 0 or F == 0:
        return 'impossible'
    if M == 1:
        return gen + F - 1
    if F == 1:
        return gen + M - 1
    
    # Traceback by dividing: gen += remainder
    if (M < F):
        small = M
        large = F
    else:
        small = F
        large = M
    new = large % small
    gen += large / small
    return BombBaby(new, small, gen)

import random
for x in range(10):
    x = random.randint(1,(10**50) + 1)
    y = random.randint(1,(10**50) + 1)
#print(x, y, answer(x, y))
#print(10**50)
print(answer(2,4))
