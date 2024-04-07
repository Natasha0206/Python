# numbers and special characters in the string and print them

email = input("Enter your email:")
alphabets = 0
special = 0
num_count = 0

for char in email:
    if char.isalpha():
        alphabets+=1
    elif not char.isalnum():
        special+= 1
    elif char.isdigit():
        num_count += 1
print("Number of alphabets",alphabets)
print("Number of Special Characters",special)
print("Number of Numbers",num_count)