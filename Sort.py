Xo = 5 #input("Enter Xo : ")
X1 = 4 #input("Enter X1 : ")
X2 = 3 #input("Enter Yo : ")

Max = max(max(Xo,X1),X2)
Min = min(min(Xo,X1),X2)
middle = Xo+X1+X2-(Min+Max)

print(Max,middle,Min)