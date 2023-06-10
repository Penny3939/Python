#99乘法表
num = input().split() #2 3 
num1 = int(num[0])
num2 = int(num[1])

times_1 = 0

while times_1 < num1:
  times_2 = 0
  while times_2 < num2:
    print(f"{times_1+1}*{times_2 +1} = {(times_1+1)*(times_2 +1)}")
    
    times_2 += 1

  times_1 += 1