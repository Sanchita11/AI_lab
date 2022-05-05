banana = int(input("Bananas : "))
capacity = int(input("Capacity of camel : "))
distance = int(input("Distance to be travelled : "))
rem = banana
used = 0
for i in range(distance):
  while(rem>0):
    rem=rem-capacity
    if rem==1:
      used = used-1
    used = used+2
  used = used-1
  rem = banana-used
  if rem==0:
    break
print("Remaining bananas :", rem)