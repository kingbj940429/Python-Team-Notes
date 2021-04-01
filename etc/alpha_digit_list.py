import string

print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters) # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 숫자 0123456789

start = ord('a')
end = ord('z')

for index in range(start, end+1):
    print(chr(index), end='')