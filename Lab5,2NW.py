# Lab 5.2 

list1 = [1,4,6,9,5,3,0]
list2 = [9,4,6,9,5,3,2]

def BiggerNum(list, TestValue):

  counter = 0
  for x in list:
    if (TestValue>x):
      counter += 1
  print counter
  
BiggerNum(list1, 3)

BiggerNum(list2, 9)