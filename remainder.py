Number = 3456

unit = Number%10
tenth = (int(Number/10))%10
hunderth = (int(Number/100))%10
thousandth = (int(Number/1000))%10

print(thousandth,",",hunderth , "," ,tenth , "," , unit)