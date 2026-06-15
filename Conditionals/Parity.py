def main():
    x = int(input("enter x :"))
    if is_even(x):
        print("even")  
    else:
        print("odd")       
#using bools
def is_even(n):
    # return n % 2 == 0

    #return True if n % 2 == 0 else False 
    
    if n % 2 == 0:
        return True
    else:
        return False     

main()

#x = int(input(" enter x :"))

#if x % 2  == 1:
    #print("odd")

#else:
    #print("even")    
