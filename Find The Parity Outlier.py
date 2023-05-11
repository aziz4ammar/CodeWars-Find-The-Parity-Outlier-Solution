def find_outlier(integers):
    # Count the number of even and odd integers
    even_count = 0
    odd_count = 0
    for num in integers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Check which parity has the outlier and return it
    if even_count > odd_count:
        for num in integers:
            if num % 2 == 1:
                return num
    else:
        for num in integers:
            if num % 2 == 0:
                return num
