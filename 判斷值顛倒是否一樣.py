# Palindrome Number 判斷值顛倒是否一樣
x = int(input())

if x <0 or (x!=0 and (x%10==0 )):
  print ("false")

x_reversed = 0
x_ori = x

while x>0:
    last_num= x%10
    x_reversed = x_reversed*10 +last_num
    x=x//10
print(x_reversed)
if x_reversed == x_ori:
  print("true")
else:
  print("false")

# string= str(a)
# left=0
# right = len(string)-1
# while left <right:
#   if string[left]!= string[right]:
#     print("false")
#   else:
#     print("true")
#   left+=1
#   right-=1

