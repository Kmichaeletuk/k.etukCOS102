entry = 0
sum1 = 0
print("Enter numbers to find their sum, negative number ends the loop:")
while True:
#int() typecasts string to integer
 entry = int(input())
if (entry < 0):
 
 sum1 += entry
print("Sum =", sum1)