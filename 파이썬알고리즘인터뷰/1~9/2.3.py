

# using '[:] = s[::-1]' (amazing trick!)

def reverseString(s:list[str])-> None:
    s[:] = s[::-1] # using same space (in-place)
    # s = s[::-1] # using different space (out-place)