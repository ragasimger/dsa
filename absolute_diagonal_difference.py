def diagonalDifference(arr):
    '''
        x = [
            1 2 3
            4 5 6
            9 8 9
        ]

    Let's understand the array as matrix here.
    The diagonal will go from indexing 0 and the first array will start from 0.
    Understand like this:
        I need biscuit[value] from container [sub array/index] of biscuits[main array].
    We'll need first data of first array, second data of second array, third data of third array 
    and it goes like this until the end which makes the diagonal.

    And from the right side, we just need to flip the coin. That means reversing the array.
    '''
    left = 0
    right = 0
    for i,v in enumerate(arr):
        left += v[i]
    arr = reversed(arr)
    for i,v in enumerate(arr):
        right += v[i]
    return abs(left-right)
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)


def diagonalSum(mat):

    '''
        Evaluating the sum of diagonal 
        elements from the array excluding 
        the crossing element.


        ####
        The diagonal crossing element will be 
        in only odd size matrices 
        ####


        Input: mat = 
            [
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
            ]
        Output: 8
    '''
    sum_ = 0
    for i, v in enumerate(mat):
        sum_ += v[i]
    for i, v in enumerate(reversed(mat)):
        sum_ += v[i]

    if len(mat) % 2 != 0:
        x = mat[len(mat)//2][len(mat)//2]
        sum_ -= x

    return sum_


    # n = len(mat)
    # sum_ =0
    # for i in range(n):
    #     sum_ += mat[i][i]
    #     sum_ += mat[i][n-i-1]
    
    # if n%2==1:
    #     sum_ -= mat[n//2][n//2]
    # return sum_