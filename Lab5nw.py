#Lab 5.1
def aList():
 aList = [66, 2, 3, 7, 86, 5, 9, 6, 68, 12, 88]
 for num in aList:
   if num % 2 == 0:
    print num
 aList.remove(7)
 for n in aList:
   if n + 1 == 68:
     aList.insert(8)
 
 print aList
 aList.sort()
 
 
 List2 = []
 
 for x in aList:
  n = x*2 
  List2.append(n)
  
aList()
 
 
