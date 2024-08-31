try:
    with open('files.txt','r') as file1:
        data = file1.read().splitlines()
        print(data)
except FileNotFoundError:
    print("File not found")
finally:
    file1.close()

