
import csv
with open('iris.data.txt', 'r') as csvfile:
	lines = csv.reader(csvfile)
	for row in lines :
		print (', '.join(row))
         
import random
"""
loadDataset
"""
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(list(dataset[x]))
	        else:
	            testSet.append(list(dataset[x]))               
	    return  trainingSet ,testSet
            
    
trainingSet=[]
testSet=[]
loadDataset('iris.data.txt', 0.8, trainingSet, testSet)
print ('Train: ' + repr(len(trainingSet)))
print ('Test: ' + repr(len(testSet)) )
print(trainingSet)

"""
euclideanDistance
"""
import math
def euclideanDistance(instance1, instance2, length):
    k=0
    for i in range(length):
        k=(instance1[i]-instance2[i])**2+k
    return math.sqrt(k)

data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print('Distance: ' + repr(distance))


"""
getNeighbors
"""
import operator
def getNeighbors(trainingSet, testInstance, k):

	distances = []

	length = len(testInstance)-1

	for x in range(len(trainingSet)):

		dist = euclideanDistance(testInstance, trainingSet[x], length)

		distances.append((trainingSet[x], dist))

	distances.sort(key=operator.itemgetter(1))

	neighbors = []

	for x in range(k):

		neighbors.append(distances[x][0])

	return neighbors





trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]

testInstance = [5, 5, 5]

k = 1

neighbors = getNeighbors(trainSet, testInstance, 1)

print(neighbors)


"""
getResponse
"""
def getResponse(neighbors):

	classVotes = {}

	for x in range(len(neighbors)):

		response = neighbors[x][-1 ]
		if response in classVotes:
			classVotes[response]=classVotes[response]+1
		else:
			classVotes.update({response : 0})
            
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)

	return sortedVotes[0][0]

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]

response = getResponse(neighbors)

print(response)


"""
getAccuracy
"""
def getAccuracy(testSet, predictions):
    correct=0
    for i in range(len(predictions)):
        if predictions[i]==testSet[i][-1]:
            correct+=1
            
        

    return (correct/float(len(testSet))) * 100.0

testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)


"""
main
"""

loadDataset('iris.data.txt', 0.8, trainingSet, testSet)
response=[]
for i in range(len(testSet)):
    neighbors=getNeighbors(trainingSet, testSet[i], 1)
    response.append(getResponse(neighbors))


accuracy=getAccuracy(testSet, response)
print(accuracy)


"""
Another distance metric(Minkowski)
"""

def MinkowskiDistance(instance1, instance2, length,p):
    k=0
    for i in range(length):
        k=(instance1[i]-instance2[i])**p+k
    return k**(1/float(p))



def getNeighbors2(trainingSet, testInstance, k,p):

	distances = []

	length = len(testInstance)-1

	for x in range(len(trainingSet)):

		dist = MinkowskiDistance(testInstance, trainingSet[x], length,p)

		distances.append((trainingSet[x], dist))

	distances.sort(key=operator.itemgetter(1))

	neighbors = []

	for x in range(k):

		neighbors.append(distances[x][0])

	return neighbors



loadDataset('iris.data.txt', 0.8, trainingSet, testSet)
response=[]
for i in range(len(testSet)):
    neighbors=getNeighbors2(trainingSet, testSet[i], 1,2)
    response.append(getResponse(neighbors))


accuracy=getAccuracy(testSet, response)
print(accuracy)



