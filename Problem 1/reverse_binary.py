"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name:
Lab Time:

"""
def reverse_binary():
    x = int(input("Enter a positive integer: "))
    binary_string = ""

    while x > 0:
        binary_string += str(x % 2)
        x //= 2

    print(binary_string[::-1])

if __name__ == "__main__":
    reverse_binary()
