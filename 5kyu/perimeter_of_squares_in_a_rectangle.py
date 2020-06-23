def perimeter(n):
    square_perimeter = [0, 4]
    for i in range(n):
        square_perimeter.append(square_perimeter[-1] + square_perimeter[-2])
    return sum(square_perimeter) 
