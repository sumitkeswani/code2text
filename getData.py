

def getData(path):
	pairData = []
	with open(path, "r") as f:
		lines = f.readlines()
		for data in lines:
			temp = data.strip().split('\t')
			summary = temp[2]
			code = temp[3]
			pairData.append([code, summary])
	return pairData




if __name__ == "__manin__":
	trainPath = "./data/stackoverflow/csharp/train.txt"
	testPath = "./data/stackoverflow/csharp/text.txt"

	pairData = getData(trainPath)
