#reversed反轉順序
num= [1,2,3,4]
print(num[::-1])

a= [1,2,3,4,5,6]
a_re = list(reversed(a))
print(a_re)
print("-"*20)
#----------------------
for i in reversed(range(1,6+1)):
  print(i)
  print(type(i))
print("-"*20)
#----------------------
b=["g","h","j","k"]
# b_st = reversed(b)

for i in reversed(b):
  print(i)
  print(type(i))