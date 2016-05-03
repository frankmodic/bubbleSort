import datetime
now = datetime.datetime.now()
import random    
arr = []

for i in range (100):    
	arr.append(random.randrange(0, 10000))
print (arr)   

def sort(unsorted):
	length = len(unsorted) - 1
	sorted = False 
	#list is unsorted and we need to sort it!

	while not sorted:
		sorted = True
		#while list is unsorted >>>
		#iterate through arr to compare each value
		for i in range(length):
			if unsorted[i] > unsorted[i +1]:
				sorted = False
				#check IF values should be swapped and if so, swap them by packing tuple
				unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
				#swap(arr[i], arr[i+1])
sort(arr)
print arr
now1 = datetime.datetime.now() - now
print "Sorting this list took:", now1, "microseond(s)"