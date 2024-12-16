import numpy as np

def edit_distance_matrix(word1, word2):
    # Initialize the distance and direction matrices
    distance = np.zeros((len(word1) + 1, len(word2) + 1, 2), dtype=int)
    distance[0, :, 0] = np.arange(len(word2) + 1)  # Initialize distances
    distance[:, 0, 0] = np.arange(len(word1) + 1)  # Initialize distances
    distance[0, :, 1] = 1  # Initialize directions
    distance[:, 0, 1] = 2  # Initialize directions

    # Compute minimum edit distances and directions
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # Diagonal value (substitution)
            if word1[i - 1] != word2[j - 1]:
                diagonal_value = distance[i - 1, j - 1, 0] + 2
            else:
                diagonal_value = distance[i - 1, j - 1, 0]  # No cost for match

            # Horizontal and vertical values (insertion and deletion)
            horizontal_value = distance[i - 1, j, 0] + 1  # Insertion cost
            vertical_value = distance[i, j - 1, 0] + 1    # Deletion cost

            # Minimum cost assignment
            if diagonal_value <= horizontal_value and diagonal_value <= vertical_value:
                distance[i, j, 0] = diagonal_value
                distance[i, j, 1] = 0  # Diagonal direction
            elif horizontal_value <= diagonal_value and horizontal_value <= vertical_value:
                distance[i, j, 0] = horizontal_value
                distance[i, j, 1] = 1  # Horizontal direction
            else:
                distance[i, j, 0] = vertical_value
                distance[i, j, 1] = 2  # Vertical direction

    return distance

def traverse(distance): 
    letter_order = []
    i = distance.shape[0]-1
    j = distance.shape[1]-1
    while j >= 0 and i >=0:
        while j >= 0 and i >=0:
            if distance[i, j, 1] == 0:
                letter_order.append(0)
                i -= 1
                j -= 1
            elif distance[i, j, 1] == 1:
                letter_order.append(1)
                j -= 1
            else:
                letter_order.append(2)
                i -= 1
    
    letter_order = letter_order[::-1]
    return letter_order[1:]

if __name__ == "__main__":
    str1 = "execution"
    str2 = "intention"
    distance = edit_distance_matrix(str1, str2)
    order = traverse(distance)
    print(order)
    # [2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0]