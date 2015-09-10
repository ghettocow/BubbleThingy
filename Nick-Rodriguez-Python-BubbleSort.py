import random
import time

start = time.time()
newArr = []

# populating the list
# -------------------
for x in range(100):
	yolo = random.randint(1,10000)
	newArr.append(yolo)

# creep through the array! not list! array!
# -----------------------------------------
limit = len(newArr) - 1
for passes in range(limit, 0, -1):
	for i in range(passes):
		if newArr[i] > newArr[i + 1]:
			(newArr[i], newArr[i + 1]) = (newArr[i + 1], newArr[i])
end = time.time()

# printing the list out w/ processing time
# ----------------------------------------
print "Bubble Sorted List:\n", newArr
print "Time to complete sort:\n", end - start, "seconds"