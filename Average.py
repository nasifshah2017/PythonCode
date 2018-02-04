#define a function cqalled my_average to calculate the average of numbers within the range of start and end
#parameters: start, end
def my_average (start, end):
 sum = 0
 count = 0
 for num in range (start, end+1):
  sum = sum + num
  count = count + 1
  print count, num, sum
 return sum/count