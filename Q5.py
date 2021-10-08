from typing import Dict


lst=[1,2,3,4,5,6,7,'t',9]
#evens=list(filter(lambda x:x%2==0,lst))
#odds=list(filter(lambda x:x%2 !=0,lst))
#print(evens)
#print(odds)
try:

    new_dict=dict(zip(filter(lambda x:x%2==0,lst), filter(lambda x:x%2 !=0,lst)))
    print(new_dict)
except TypeError:
    print("Enter the integer value in list")
#new=dict(zip(evens,odds))
#print(new)