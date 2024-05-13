def space(): #To make it look good
    print()
    print("**********************************************************")
    print()

def prime(a):
    space()
    for b in range(2,a):
        if a%b==0:
            print("The number",a," is not a prime")
            break
    else:
        print("The number",a," is a prime")

def palindrome(a):
    space()
    a=str(a)
    mid=int(int(len(a))/2)
    rev=-1
    for b in range(0,mid+1):
        if a[b]!=a[rev]:
            print("The number",a," is not a palindrome")
            break
        else:
            rev=rev-1
    else:
        print("The number",a," is a palindrome")
        
def table(a):
    space()
    print("The tables of the number",a,"are as presented below:")
    print()
    for b in range(1,11):
        print(a,"x",b,"=",a*b)
    
choice=0

while choice!=5:
    print("Please select from one of the options below")
    print("1)Do you want to find the following: Prime number,plaindrome and multiplication")
    print("2)Do you want to check whether it is prime number or not")
    print("3)Do you want to check whether it is palindrome or not")
    print("4)Do you want to print its table")
    print("5)To exit the code")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        number=int(input("Enter a number"))
        prime(number)
        palindrome(number)
        table(number)
        
    elif choice==2:
        number=int(input("Enter a number"))
        prime(number)
        
    elif choice==3:
        number=int(input("Enter a number"))
        palindrome(number)
        
    elif choice==4:
        number=int(input("Enter a number"))
        table(number)
        
    space()
    