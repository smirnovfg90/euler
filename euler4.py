def isPol(prod):
    strProd = str(prod);
    length = len(strProd);
    for i in range(0,int(length/2)):
        if(strProd[i]!=strProd[length-i-1]):
            return 0;
    return 1;

maxProd = 0;    
for i in range(100,999):
    for j in range(100,999):
        prod = i * j;
        if(isPol(prod)):
            if(prod>maxProd):
                maxProd=prod;
print(maxProd);
        
