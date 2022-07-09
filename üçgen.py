def ucgen(x):
 
 

 if abs(x[0]+ x[1]) > x[2] and abs(x[0] + x[2]) > x[1] and abs(x[1] + x[2]) >x[0]:
    return True
 else:
    return False
     

liste = [(3,4,5),(6,8,10),(3,10,7)]


print(list(filter(ucgen, liste)))



