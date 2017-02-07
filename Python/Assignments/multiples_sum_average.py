a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
for count in range(1, 1000):        #print odd integers from 1 - 1000
    if count % 2 == 1:
        print count
for count in range (5,1000000):     #print multiples of 5 from 5 - 1,000,000
    if count % 5 == 0:
        print count
for element in a:                   #sum up each element then print
    sum += element
print sum
avg = sum / len(a)                  #use len() list function to get divisor
print avg
