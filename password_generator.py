import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

while True:
    num_of_char = input("how many characters ? ")
    num_of_char = int(num_of_char)
    if num_of_char < 6:
        print("at least 6 charcters !")
        continue
    else:
        break

p1 = random.choices(s1,k=(round(num_of_char*30/100)))
p2 = random.choices(s2,k=(round(num_of_char*27/100)))
p3 = random.choices(s3,k=(round(num_of_char*19/100)))
p4 = random.choices(s4,k=(round(num_of_char*19/100)))
pasw = p1 + p2 + p3 + p4
random.shuffle(pasw)
passw = "".join(pasw)
print(passw)

