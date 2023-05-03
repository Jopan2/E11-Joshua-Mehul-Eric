def dot(locs, counts):
    mapper = []
    for i in enumerate(locs):
        temp = [locs[i]] * int(counts)
        mapper.extend(temp) 
    return mapper
    
locs = [1,2,3,4,5]
counts = [1,2,3,4,5]

print(dot(locs,counts))