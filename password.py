import numbers
import random

lower_case="abcdefghijkhlmnopwxyz"
upper_case="ABCDEFGHIJKLMNOPWXYZ"
numbers="123456789"
synbols="@#$%-_*^&"

creation=lower_case+upper_case+numbers+synbols
length_ofpass=int(input("hello sir hope ur having a good day give us the length of ur new  generated password : "))
passwrod="".join(random.sample(creation,length_ofpass))
print("ur password is :",passwrod)
