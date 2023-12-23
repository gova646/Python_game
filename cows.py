
def get_cows(source_number,check_number):
    '''returns the number of matching literals in both the inputs'''
    cows = 0
    bulls = 0
    for i in range(0,len(source_number)):
        for j in range(0,len(source_number)):
            if source_number[i] == check_number[j]:
                if i == j:
                    cows = cows + 1
                else:
                    bulls = bulls + 1
    cows_bulls = [cows,bulls]
    return cows_bulls

