def group_groceries(groceries):
    sorted_groceries = {"fruit":[], "meat":[], "other":[],"vegetable":[]}
    for item in groceries.split(","):
        category,name=item.split("_")
        if category in sorted_groceries:
            sorted_groceries[category].append(name)
        else:
            sorted_groceries["other"].append(name)
    for category in sorted_groceries:
        sorted_groceries[category]=",".join(sorted(sorted_groceries[category]))
    return "\n".join([category+":"+list for category,list in sorted_groceries.items()])
