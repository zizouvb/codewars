def sum_of_intervals(intervals):
    items = set()
    for interval in intervals:
        items.update(range(interval[0],interval[-1]))
    return len(items)
