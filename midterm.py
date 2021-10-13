from math import dist

def question2():
    list_a = [0,0,0,1,0,1,0,1,0,0]
    list_b = [0,0,0,1,0,1,1,0,0,0]
    a,b,c,d = 0,0,0,0
   
    for i,j in zip(list_a, list_b):
        if i == 1 and j == 1:
            a += 1
            
        elif i == 0 and j == 1:
            b += 1
        
        elif i == 1 and j == 0:
            c += 1
        
        else:
            d += 1
            
    return ((b+c)/(a+b+c+d))
    

def question4():
    list_a = [0,0,0,1,0,1,0,1,0,0]
    list_b = [0,0,0,1,0,1,1,0,0,0]
    a,b,c,d = 0,0,0,0
   
    for i,j in zip(list_a, list_b):
        if i == 1 and j == 1:
            a += 1
            
        elif i == 0 and j == 1:
            b += 1
        
        elif i == 1 and j == 0:
            c += 1
        
        else:
            d += 1
            
    return ((b+c)/(a+b+c))

def question6():
    a = [.5, .5]
    b = [1, 1]
    return dist(a,b)

def question8():
    a = [.5, .5]
    b = [1, 1]
    r = 1
    res = 0
    for i,j in zip(a,b):
        res += abs(j-i)**r
    
    return pow(res,1/r)

def question12():
    P = [1,0,0,0,0,0,0,0,0,0] 
    Q = [0,0,0,0,0,0,1,0,0,1]
    f00, f11, f01, f10 = 0,0,0,0

    for i,j in zip(P,Q):
        
        if i == 0:
            if j == 1:
                f01 += 1
            
            else:
                f00 += 1
                
        else:
            if j == 1:
                f11 += 1
            
            else:
                f10 += 1
        
    return ((f00 + f11)/(f00 + f01 + f10 + f11))

def question14():
    P = [1,0,0,0,0,0,0,0,0,0] 
    Q = [0,0,0,0,0,0,1,0,0,1]
    f00, f11, f01, f10 = 0,0,0,0

    for i,j in zip(P,Q):
        
        if i == 0:
            if j == 1:
                f01 += 1
            
            else:
                f00 += 1
                
        else:
            if j == 1:
                f11 += 1
            
            else:
                f10 += 1
        
    return ((f11)/(f01 + f10 + f11))

def main():
    print(question2())
    print(question4())
    print(question6())
    print(question8())
    print(question12())
    print(question14())


if __name__ == "__main__":
    main()