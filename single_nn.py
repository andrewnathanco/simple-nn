import numpy as np
import random as rand


def sigmoid(x):
	return np.exp(x)/(np.exp(x)+1)

def sigmoidDerivative(x):
	return x * (1-x)

def sign(x):
	if x >= 0:
		return 1
	else:
		return -1
class NeueralNet():
	def __init__(self):
		self.weights = [rand.uniform(-1,1)] * 2

	def guess(self):
		self.sum = 0
		for i in range(self.lengthx):
			self.sum += self.x[i] * self.weights[i]
		self.output = sign(self.sum)
		return self.output

	def train(self,x,target):
		self.lengthx = len(x)
		self.lengthy = len(target)
		self.x = x
		self.y = target[0]
		self.numberGuess = self.guess()
		self.error = self.y - self.numberGuess

		for i in range(len(self.weights)):
			self.weights[i] += self.error * self.x[i]



def main():
	with open('sing_nn_training_data.csv') as file:
		file.readline()

		fileList = file.readlines()
		newFile = []
		for line in fileList:
			newLine = line.rstrip('\r\n')
			newFile.append(newLine.split(','))

		NN = NeueralNet()
		# i = 0
		probSum = 0

		for line in newFile:

			# i += 1

			inputArray = [int(line[0]),int(line[1])]
			outputArray = [int(line[2])]


			# print('Input X/Y: ')
			# print(inputArray)
			# print('Correct Answer ')
			# print(outputArray)


			NN.train(inputArray,outputArray)


			# print('Computer Guess')
			# print(NN.numberGuess)

			# print('Success #:', i)

			if int(line[2]) == NN.numberGuess:
				probSum += 1

		print('Probability of Correct: ')		
		print(float(probSum) / float(len(newFile)) * 100)




main()