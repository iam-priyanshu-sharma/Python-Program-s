result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]

print(result)
