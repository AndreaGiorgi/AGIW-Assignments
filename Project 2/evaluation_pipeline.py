
def eval(S1S2Pairs):

		totalPairs = 0  
		elementsEvalued = 1 
		precisionValue = 0 
		recallValue =0 
		f1Value = 0
		
		for pair in S1S2Pairs:
			if pair[0] == pair[1]:
				totalPairs +=1
			precisionValue = totalPairs/elementsEvalued
			recallValue = totalPairs/50
			f1Value = 2*(recallValue*precisionValue)/(recallValue+precisionValue)
			elementsEvalued += 1

		print("Total pairs found: " + str(totalPairs))
		print("Precision: " + str(precisionValue))
		print("\nRecall: " + str(recallValue))
		print("\nF1: "+ str(f1Value) + '\n')
  
def evaluation_pipeline(pairs):
    eval(pairs)