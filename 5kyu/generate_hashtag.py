def generate_hashtag(s):
    input = s.title().replace(" ","")    
    if len(input)>140 or len(input)==0:
        return False
    return "#" + input
