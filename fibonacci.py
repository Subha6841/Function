# program to find a fibonacci series

# ----- defining the function--------
def fibonacci_series(x,y):
    print('The fibonacci series is')
    if n==0:
        print(0)
    elif n==1:
        print(x)
    else:
        print(x)
        print(y) 
        for i in range(2,n):
            sum1=x+y
            print(sum1) 
            x=y
            y=sum1          
            
#  -------- defining the program -------
n=int(input('Enter the no. of element of the Fibonacci series : '))
a=int(input('Enter the first element of the series : '))
b=int(input('Enter the second element of the series : '))
fibonacci_series(a,b)

            

        
            
    
    
