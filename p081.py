import time

start = time.time()

def minCost(cost, row, col):
    
    # For 1st column
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]

    # For 1st row
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]

    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            cost[i][j] += min(cost[i][j - 1], cost[i - 1][j])
#             print(cost[i][j])
    
    # Returning the value in
    # last cell
    return cost[row - 1][col - 1]

# Driver code
if __name__ == '__main__':
    
    cost = [  [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150], 
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956], 
            [805, 732, 524, 37, 331]   ]

    matrix_file = open('p81_matrix.txt', 'r')
    matrix = matrix_file.readlines()
    cost = []

    for row in matrix:
        cost.append(list(map(int, row.split(','))))

    row = col = len(cost)	
    print(minCost(cost, row, col))
    print(time.time() - start)

