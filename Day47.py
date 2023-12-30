#  Write Program to find longest palindrome in an array
def check(n):

   div = 1

   while (int(n / div) >= 10):

      div *= 10

   while (n != 0):

      front = int(n / div)

      rear = n % 10

      if (front != rear):

        return False

      n = int((n % div) / 10)

      div = int(div / 100)

   return True

 

def largestPal(arr, n):

   result = -1

 

   for i in range(0, n, 1):

      if (arr[i] > result and check(arr[i])):

         result = arr[i]

 

   return result
n = int(input("Enter the size of array: "))
arr=[]
count=0
for i in range(0,n):
    m=int(input("enter the elements: "))
    arr.append(m)
print("Longest palindrome:",largestPal(arr,n))