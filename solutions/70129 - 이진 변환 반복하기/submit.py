def solution(s, c=0, z=0):    
    while len(s) > 1 and (c := c + 1):
        z += len(s) - (o := s.count("1"))
        s = bin(o)[2:]    
    return c, z
