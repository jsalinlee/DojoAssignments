def odd_even(rangeAnd1):
    for count in range(1, rangeAnd1):
        if count % 2 == 1:
            print "Number is " + str(count) + ". This is an odd number."
        if count % 2 == 0:
            print "Number is " + str(count) + ". This is an even number."
def multiply(array, multiplier):
    index = 0;                              #keep an index variable, set
    for element in array:                   #array element to element * multiplier'''
        array[index] = element * multiplier
        index += 1
    return array
def layered_multiples(arr):
    fill = 1
    print arr
    ones_array = []                     #the element array to be filled with ones
    new_array = []
    for element in arr:                 #for each element in array
        for count in range(element):    #loop up to the element value
            ones_array.append(fill)     #append 1 every increment
        new_array.append(ones_array)    #append array of ones into new_array
        ones_array = []                 #reset ones_array to catch next array of ones
    return new_array

odd_even(2001)
ex = multiply([2,4,10,16], 5)
print ex
x = layered_multiples(multiply([2,4,5],3))
print x
