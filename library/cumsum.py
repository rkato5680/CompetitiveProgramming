# compute cumulative sum of the given sequence

def cumsum(array):
    new=[0]
    for i in range(len(array)):
        new.append(array[i]+new[-1])
    return new
