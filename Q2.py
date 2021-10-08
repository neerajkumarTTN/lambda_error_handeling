def is_prime(num):
    if num >= 2:
        for y in range(2,num):
            if num%2==0:
                return False
            else:
                return True
    else:
	    return False
    return True
    
#num=[5,3,4,6,7]
num=[33]
print(list(filter(is_prime,num)))