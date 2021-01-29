import random

passlen = int(input(" Enter length of the Password  "))
string="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pas = "".join(random.sample(string , passlen ))
print (pas)