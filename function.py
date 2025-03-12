def Add(numbers):
    if not numbers:
        return 0
    elif ",\n" in numbers or "\n," in numbers:
        return -1 
    
    numbers = numbers.replace("\n", ",")

    if numbers.startswith(",") or numbers.endswith(","):
        return -1
    
    numbers_list = map(int, numbers.split(","))

    return sum(numbers_list)