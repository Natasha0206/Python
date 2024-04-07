# ask user for name and return a mail id in the format 
# 'username@gmail.com' and print it 


username = input("Enter username:")
def email(username):
    return username + "@gmail.com"
mail = email(username)
print(mail)