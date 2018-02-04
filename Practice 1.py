def my_avg(start,end):
 sum = 0
 count = 0
 for num in range (start,end+1):
  sum += num
  count += 1
 #print num, sum, count
 print sum/count
 return sum/count 
 
my_avg(3,7)
 

def my_mult (a,b):
 print a*b
 return a*b

my_mult (5,5)
my_mult (3,10)
 
list1 = [3,4,7,8,2,1,9]
list2 = [1,5,8,3,5,6,7]

def BiggerNum(list, TestValue):

 counter = 0
 for x in list:
  if (x>TestValue):
   counter += 1
 print counter

BiggerNum(list1, 6) 

hourly_rate = 11
hours_per_week = 40

Salary_per_week = hourly_rate * hours_per_week
print Salary_per_week

def aList():
 aList = [66, 2, 3, 7, 86, 5, 9, 6, 68, 12, 88]
 for num in aList :
  if num % 2 == 0:
   print num
 aList.remove(7)
 aList.insert(8)
 aList.sort()
 