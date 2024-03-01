"""
Complete the following python code to reverse the string entered by the user.

Name: 
Lab Time:
"""

def reverse_string():
    while True:
        user_input = input("Enter a line of text (or 'Done' to exit): ")
        if user_input.lower() in ["done", "d"]:
            break
        reversed_text = user_input[::-1]
        print(reversed_text)

if __name__ == "__main__":
    reverse_string()
