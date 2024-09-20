# Program to find the element not making a pair
# Function to calculate the number that is odd occuring
def oddoccurence(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
# Initialize our array
arr = []
# Take array size as input
n = int(input("Enter array size:"))
# Take array element input
while(n):
    num = int(input("Enter number:"))
    arr.append(num)
    n -= 1
print("\n \n Odd occuring number is:", oddoccurence(arr))        