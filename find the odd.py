def find_it(seq):
    elems = {}
    for num in seq:
        if num in elems:
            del elems[num]
        else:
            elems[num]=1
    return [*elems][0]
