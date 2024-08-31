def Fibonacci(n):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(1,n):
        temp = num1+num2
        print(temp)
        num1=num2
        num2=temp
       
def FibonacciWord(n):
    num1="a"
    num2="b"
    print(num1)
    print(num2)
    for i in range(1,n):
        temp = num1+num2
        print(temp)
        num1=num2
        num2=temp

FibonacciWord(10)
    
