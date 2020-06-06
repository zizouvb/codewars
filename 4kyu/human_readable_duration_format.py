def format_duration(seconds):
    duration = {"year":365*24*3600, "day":24*3600, "hour":3600, "minute":60,"second":1}
    items=[]
    if seconds==0:
        return "now"
    for title, duration in duration.items():
        value = seconds//duration
        if value>1:
            items.append(str(value) + " " + title + "s")
        elif value>0:
            items.append(str(value) + " " + title)
        seconds %= duration
    if len(items)>1:
        return ", ".join(items[:-1]) + f" and {items[-1]}"
    return items[0]
