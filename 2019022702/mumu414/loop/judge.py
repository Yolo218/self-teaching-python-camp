# 使用 while 循环判断输入的数字是奇数还是偶数，并打印出来，是0时退出循环

i=int(input("输入一个数字："))
while i >=0 : 
   
   if i==0: 
       print("输入为0 退出")
       break
   if i%2==0:
       print(i,"是偶数")
       i= int(input("输入一个数字："))
       continue
   else:
       print(i,"是奇数")
       i= int(input("输入一个数字："))
       continue
 
    