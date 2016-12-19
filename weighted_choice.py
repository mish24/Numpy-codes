def find_interval(x, 
                  partition, 
                  endpoints=True):
    """ find_interval -> i
        If endpoints is True, "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        
        If endpoints is False, "i" will be the smallest index 
        for which applies x < partition[i]. If no such index exists 
        "i" will be set to len(partition)
    """
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1 if endpoints else i
    return -1 if endpoints else len(partition)
I = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
print("Endpoints are included:")
for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I))
print("\nEndpoints are not included:")
for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I, endpoints=False))

