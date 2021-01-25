#array = list(map(int,input().split(",")))
#k = int(input())

# Example input : 10,20,30,40,50
# k : 3
array = [1,2,3,4,5,6,7]
k = 3

# method 1
def rotate1(array,k):
    for i in range(k):
        array = [array[-1]] + array[:-1]
    return array

#method 2
def rotate2(array, k):
    for i in range(k):
        array.insert(0,array.pop())
    return array

print(rotate1(array,k))
print(rotate2(array,k))
