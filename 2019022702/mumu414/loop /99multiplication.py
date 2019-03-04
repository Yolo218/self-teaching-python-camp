#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
       print(i,"*",j,"=",i*j,"\t",end=" ")#end=" "表示不换行
       if i == j:
           print(" ")
           break