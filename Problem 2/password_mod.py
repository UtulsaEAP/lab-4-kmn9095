"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:
Lab Time:
"""

def password_mod():
    password = input()
    stronger_password = ''
    replacements = {'i': '1', 'a': '@', 'm': 'M', 'B': '8', 's': '$'}
    
    for char in password:
        if char in replacements:
            stronger_password += replacements[char]
        else:
            stronger_password += char
    stronger_password += '!'
    
    print(stronger_password)
    return stronger_password

# Example usage:
if __name__ == "__main__":
    password_mod()
    #stronger_password = password_mod(input_password)
    #print(stronger_password)
