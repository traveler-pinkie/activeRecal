def rotate_matrix(matrix, direction):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with swapped dimensions (cols x rows)
    # We initialize it with placeholders
    rotated = [[0] * rows for _ in range(cols)]

    if direction == "clockwise":
        for r in range(rows):
            for c in range(cols):
                # Row r becomes column (rows - 1 - r)
                rotated[c][rows - 1 - r] = matrix[r][c]
                
    elif direction == "counter-clockwise":
        for r in range(rows):
            for c in range(cols):
                # Row r becomes column r, but column c becomes row (cols - 1 - c)
                rotated[cols - 1 - c][r] = matrix[r][c]
    
    return rotated
