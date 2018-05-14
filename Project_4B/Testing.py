from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def varyPerceptrons(func):
    numPerc = 0
    maxAccs = []
    avgAccs = []
    Devs = []

    while not numPerc > 40:
        accList = []
        for iteration in range(5):
            testAccuracy = 0.0
            if not func != 0:
                nnet, testAccuracy = testPenData(hiddenLayers = [numPerc])
            elif func == 1:
                nnet, testAccuracy = testCarData(hiddenLayers = [numPerc])
            accList.append(testAccuracy)

        avgAccs.append((average(accList), numPerc))
        maxAccs.append((max(accList), numPerc))
        Devs.append((stDeviation(accList), numPerc))
        numPerc += 5

        print("Max accuracies: " + str(maxAccs))
        print("Standard deviations: " + str(Devs))
        print("Average accuracies: " + str(avgAccs))
        
varyPerceptrons(1);



