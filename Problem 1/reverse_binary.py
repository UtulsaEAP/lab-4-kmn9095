"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name:
Lab Time:

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
def reverse_binary():
    x = int(input())
    while x > 1 :
        print(str(x % 2))
        x=x/2

if __name__ == "__main__":
    reverse_binary()
