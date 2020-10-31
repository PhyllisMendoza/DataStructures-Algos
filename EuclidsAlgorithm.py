def euclid(x, y):  
    if x == 0 : 
        return y  
      
    return euclid(y%x, x)
