def greatestNumberCount(candles):
    '''
        Finding the greatest number from array
        and returning the count of that number.
    '''
    count = 0
    tallest_candle = candles[0]
    for _ in candles:
        if _ > tallest_candle:
            tallest_candle = _
        
    for _ in candles:
        if _ == tallest_candle:
            count += 1
    return count

arr = [4,4,1,3]

obj = greatestNumberCount(arr)
print(obj)