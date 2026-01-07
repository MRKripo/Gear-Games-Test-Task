def compress_numbers(array):
    if not array:
        return []
    
    current_number = array[0]
    result = [array[0]]

    for i in array[1:]:
        if i != current_number:
            result.append(i)
            current_number = i
    
    return result