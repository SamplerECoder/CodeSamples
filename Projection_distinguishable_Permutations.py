#%%
from itertools import permutations

n=4
#%%
"""
Permutations are given as list!
"""
def conflict_free(a,b):
    for i in range(len(a)):
        a_ = a.copy()
        b_ = b.copy()
        a_.remove(i)
        b_.remove(i)
        if (a_ == b_):
            return False
        
    return True
        
        
#%%
n=6
current_set = []
for permutation in [list(x) for x in permutations(range(n))]:
    all_conflict_free = True
    for element in current_set:
        if not conflict_free(element, permutation):
            all_conflict_free = False
            break
    if all_conflict_free:
        current_set.append(permutation)
    else:
        continue
    
print(len(current_set))
#%%
