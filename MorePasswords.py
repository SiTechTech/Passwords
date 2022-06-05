import random

# Words = "abcdefghijklmnopqrstuvwxyz"
# Numbers = "123456789"
# Symbols = "!#$%^&*():?><"
# Caps = "ABCDEFGHIOKLMNOPQRSTUVWXYZ"

# all = Words + Numbers + Symbols + Caps
# length = 10
# password = ''.join(random.sample(all, length))
# print("The Password is Generated:", password)


# # More Common use

Words = "abcdefghijklmnopqrstuvwxyz"
Numbers = "123456789"
Caps = "ABCDEFGHIOKLMNOPQRSTUVWXYZ"

all = Words + Numbers + Caps
length = 10
password = ''.join(random.sample(all, length))
print("The Password is Generated:", password)
