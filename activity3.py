print('Enter marks obtained in 5 subjects')
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
sum=m1+m2+m3+m4+m5
avg=sum/5
if avg>90:
    print('o grade')
elif avg>80:
    print('A grade') 
elif avg>70:
    print('B grade') 
elif avg>40:
    print('C grade')
else:
    print('Not qualified')     
