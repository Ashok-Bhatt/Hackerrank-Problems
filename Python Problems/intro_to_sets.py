def average(array):
    height = sum(set(array))
    number = len(set(array))
    average = round(height/number,3)
    return average

