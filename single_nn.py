import random as rand


'''
Name: Andrew Cohen
Date: 7/17
File Name: single_nn.py
'''

#Create a simple activation function
def sign(x):
	if x >= 0:
		return 1
	else:
		return -1


#Organize the neural net with a class structure
class NeueralNet():
	def __init__(self):
		self.weights = [rand.uniform(-1,1)] * 2

	def guess(self,x):
		self.x = x
		self.lengthx = len(x)
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
		self.numberGuess = self.guess(self.x)
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
		i = 0
		probSum = 0

		for line in newFile:

			i += 1

			inputArray = [int(line[0]), int(line[1])]
			outputArray = [int(line[2])]


			# print('Input X/Y: ')
			# print(inputArray)
			# print('Correct Answer ')
			# print(outputArray)


			NN.train(inputArray,outputArray)

			# print('Computer Guess')
			# print(NN.numberGuess)

			# print('Success #:', i)

			if int(int(line[2])) == NN.output:
				probSum += 1

		print('Probability of Correct Using Training Data: ')		
		print(float(probSum) / float(len(newFile)) * 100)
			

		probSum = 0
		for i in range(100):
			testInput = [rand.randint(1,100),rand.randint(1,100)]
			if testInput[1] / testInput[0] >= 1:
				testAnswer = 1
			else:
				testAnswer = -1

			NN.guess(testInput)

			# print('Computer Guess')
			# print(NN.guess(testInput))
			# print('Actual Answer')
			# print(testAnswer)

			if int(testAnswer) == NN.output:
				probSum += 1


		print('Probability of Correct Using Randomly Generated Data: ')		
		print(float(probSum) / float(100) * 100)

main()
