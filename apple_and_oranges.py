def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''
        s -> house starting point
        t -> house ending point
        a -> apple's point
        b -> orange's point
        
        apples -> array of apples
        oranges -> array of oranges
    '''
    landed_apples = []
    landed_oranges = []
    for _ in apples:
        distance = a + _
        if distance in range(s, t+1):
            landed_apples.append(distance)
        '''
        Either of these works
        '''
        # if distance >=s and distance <= t:
        #     landed_apples.append(_)
    for _ in oranges:
        distance = b + _
        if distance in range(s, t+1):
            landed_oranges.append(distance)
        '''
        Either of these works
        '''
        # if distance >=s and distance <=t:
        #     landed_oranges.append(_)
    new_list = []
    new_list.append(len(landed_apples))
    new_list.append(len(landed_oranges))
    for _ in new_list:
        print(_)


first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)