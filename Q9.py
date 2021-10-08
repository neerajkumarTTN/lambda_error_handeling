import random
 
def roll_dice(data_list, times):
    total = 0
    for i in range(times):
        num = random.randint(1,6)
        total = total + num
        data_list[num-1] = data_list[num-1] + 1
        i+=1
    average = total * 1.0 / times
    return average    
data_list = [0, 0, 0, 0, 0, 0]
times = 10000
average = roll_dice(data_list,times)
print ("The average number rolled is",average)