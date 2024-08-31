List = [1,2,3,4,5,6,7,8,9]

sq = [i**2 for i in List]



words = ["cat", "elephant", "dog", "bird", "giraffe", "rat"]
morethanthree = [word for word in words if len(word)>3]

text = "a1b2c3d4e5"
numbers = [text[i] for i in range(len(text)) if text[i] >=1 and text[i] <=9]
print(numbers)

multiple = [i for i in range(0,50) if i%3==0 and i%5==0]

uppercase = [uppercase(word) for word in words ]

words = ["apple", "banana", "cherry", "date", "grape"]

ending_e= [word for word in words if word[-1]=="e"]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [[i for i in matrix] for j in matrix]


def multiplie():
    num = 1
    while True:
        pass
        #yeild 1*5
        #num = num +1

obj = multiple()
print(next(obj))