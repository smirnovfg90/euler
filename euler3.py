import math
def isSimple(a):
    for i in range(2,a):
        if a%i == 0:
            return 0;
    return 1;

num = math.ceil(math.sqrt(600851475143));
for i in range (3,num):
    if((600851475143%i == 0) and isSimple(i)):
        print(i);
    
        
            
