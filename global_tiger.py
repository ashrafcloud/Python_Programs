# Write a program to use Global variable 


def state1():
    global tigers
    tigers = 15
    print (tigers)

tigers=95
print(tigers)
state1()
print(tigers)
    
    
# Output                                                                                                                                                 
95                                                                                                                                                                  
15                                                                                                                                                                  
15    
