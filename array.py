
size = input("Enter the size of the array ")
print("Enter the elements of the array")
size = int(size)

arr[0] = 0

for i in range(size):
    arr[i] =  input()

print ("Array values are")
for i in range(size):
    print(arr[i])


