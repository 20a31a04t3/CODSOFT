import string
import random
length=int(input("enter the length of the password:"))
lower1=string.ascii_lowercase
upper1=string.ascii_uppercase
digit=string.digits
symbols=string.punctuation
str=lower1+upper1+digit+symbols
pwd=random.sample(str,length)
password=" ".join(pwd)
print(password)
