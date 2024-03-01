"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:
Lab Time:
"""

def strengthen_password(password):
    stronger_password = ''
    replacements = {'i': '1', 'a': '@', 'm': 'M', 'B': '8', 's': '$'}
    
    for char in password:
        if char.lower() in replacements:
            stronger_password += replacements[char.lower()]
        else:
            stronger_password += char
    stronger_password += '!'
    
    return stronger_password

# Example usage:
input_password = input("Enter a simple password: ")
stronger_password = strengthen_password(input_password)
print(stronger_password)
