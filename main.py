import random
import time

def generateLargeNumberOfBoxes(N, limit=1000):
    # code to generate n boxes with random dimensions up to limit
    boxes = []
    for _ in range(N):
        height = random.randint(1, limit)
        width = random.randint(1, limit)
        depth = random.randint(1, limit)
        boxes.append((height, width, depth))
    return boxes



def generateRotations(height, width, depth):
    # generate all possible rotations first 
    # since it is a rectangular box two sides have the same area
    # so a total of 3 distince rotations exists for each box

    return [
        (max(width, depth), min(width, depth), height),   
        (max(height, depth), min(height, depth), width),  
        (max(height, width), min(height, width), depth)   
    ]

def isStakableOnTop(bottom_box, top_box):
    # check if one box can be placed on top of another 
    # the length and width of the top box are  strictly less than those of the bottom box

    bottom_length, bottom_width, bottom_depth_ = bottom_box
    top_length, top_width, top_depth = top_box

    return bottom_length > top_length and bottom_width > top_width


def calculateMaximumHeight(boxes):

    # if given empty list of boxes return 0
    if not boxes:
        return 0, []

    # handle edge case of single box 
    # if len(boxes) == 1:
    #     rotations = generateRotations(boxes[0])
    #     tallest_rotation = max(rotations, key=lambda x: x[2])
    #     return tallest_rotation[2], [tallest_rotation]

    # generate all possible rotations for each box which is 3n
    all_possible_rotations = []
    for height, width, depth in boxes:
        all_possible_rotations.extend(generateRotations(height, width, depth))

    N = len(all_possible_rotations)

    # sort by decreasing base area (length * width) because any box that has lower area can go on top of it 
    # then we can deal with the problem using LIS 1D DP approach
    all_possible_rotations.sort(key=lambda box: box[0] * box[1], reverse=True)

    # initialize 1D DP array
    dp = [0] * N

    # new array to keep track of the box which is below the current box in the optimal stack
    track = [-1] * N 

    # each box can be at least as tall as itself
    for i in range(N):
        dp[i] = all_possible_rotations[i][2]  

    for i in range(N):
        for j in range(i):
            if isStakableOnTop(all_possible_rotations[j], all_possible_rotations[i]):
                # if the current height by placing box i on top of box j is more than the current recorded height for box i
                # update dp[i] and track[i]
                if dp[j] + all_possible_rotations[i][2] > dp[i]:
                    dp[i] = dp[j] + all_possible_rotations[i][2]
                    track[i] = j   

    # get the maximum height index and maximum height from the dp array
    max_index = max(range(N), key=lambda i: dp[i])
    max_height = dp[max_index]

    # reconstruct which boxes were used in the optimal stack
    stack = []
    curr = max_index
    while curr != -1:
        stack.append(all_possible_rotations[curr])
        curr = track[curr]

    # reverse so it goes from bottom to top
    stack.reverse() 

    return max_height, stack


if __name__ == "__main__":
    # boxes = [(1, 2, 3)]
    # testing for these N values
    n_values = [10,50,100,200,400,600,800,1000,1500,2000,3000,4000,5000,6000, 7000, 8000, 9000, 10000, 12500, 15000, 17500, 20000]

    # to see the output for different values of n just change the index of n_values[i]
    boxes = generateLargeNumberOfBoxes(n_values[0])

    start_time = time.time()
    height, stack = calculateMaximumHeight(boxes)
    end_time = time.time()
    print("Execution time is : ", end_time - start_time)

    # height, stack = calculateMaximumHeight(boxes)
    print("Maximum stack height:", height)
    print("Boxes used (bottom to top):")

    for box in stack:
        print(box)
