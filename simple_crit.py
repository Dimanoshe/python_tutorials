import simplecrypt
from urllib import request

test = simplecrypt.EncryptionException('hello!')
print(type(test))

my_file = open("some.txt", "w")
my_file.write(str(test))
my_file.close()

with open("some2.txt", 'w') as f:
    f.write('hello world')

with open("some.txt") as file:
    pass




'''encrypted = request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
password = request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()

for i in password:
    print(i)
    try:
        print(simplecrypt.decrypt(i, encrypted))
    except simplecrypt.DecryptionException:
        print('Wrong password')
        pass


print(encrypted)
print(type(encrypted))
print(password)
print(type(password))
'''
