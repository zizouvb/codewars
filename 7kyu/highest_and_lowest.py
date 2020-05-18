def high_and_low(numbers):
    lowest = float("inf")
    highest = -float("inf")
    for num in list(map(int,numbers.split(" "))):
        if num<lowest:
            lowest = num
        if num> highest:
            highest = num
    return str(highest) + " " + str(lowest)
