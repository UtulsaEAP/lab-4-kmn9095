"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name:
Lab Time:

"""


#def reverse_binary():
#    x = int(input())
#    while x > 1 :
#        print(str(x % 2))
#        x=x/2

def reverse_binary(n):
    if n == 0:
        return '0'
    
    result = ''
    while n > 0:
        result += str(n % 2)
        n //= 2
    
    return result

# Example usage:
num = int(input("Enter a positive integer: "))
print(reverse_binary(num))