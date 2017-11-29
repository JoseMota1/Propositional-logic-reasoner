# Program to convert logical sentences in propositional logic into CNF


import sys
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um 


for lines in sys.stdin:
	sentences = eval(lines) 
	recursive(sentences)

iteration = 1
myConditions = list()

def recursive(line)
	if atom (line,TRUE)

	elif line[0]=='<=>'
		equivalence(line[1],line[2])

	elif line[0]== '=>' 
		implication(line[1],line[2])

	elif line[0]=='or' 
		disjunction(line[1],line[2])	

	elif line[0]=='and'
		conjunction(line[1],line[2])

	elif line[0]=='not' 
		if neg_atom(line,TRUE)
		elif negation(line[1])

	return


def atom(sentence, value):
	if len(sentence)>1
		return FALSE
	elif len(sentence)==1
		if value == TRUE
			myConditions[iteration].append(sentence)
		return TRUE
	return

def neg_atom(sentence, value):	
	if len(sentence)==2 and sentence[0]=='not' and atom(sentence[1])
			if value == TRUE
				myConditions[iteration].append(sentence)
		return TRUE
	else
		return FALSE		
	return


def equivalence(sentence1, sentence2):
		implication(sentence1,sentence2)	
		implication(sentence2,sentence1)
	return
	
def implication(sentence1, sentence2):
	disjunction(('not', sentence1), sentence2);
	return 

def disjuntion(sentence1, sentence2):
	if (atom(sentence1,0) or neg_atom(sentence1,0)) and (atom(sentence2,0) or neg_atom(sentence2,0)) 
		if (atom(sentence1,0) and neg_atom(sentence2,0)) or (atom(sentence2,0) and neg_atom(sentence1,0)) # ignora-se.
			return
		else
			myConditions[iteration].append([sentence1, sentence2]) # not sure this is how its done
	else
		distribution(sentence1, sentence2)
	return


def distribution(sentence1, sentence2): # MERDAA
	iteration = iteration+1
	recursive(sentence1)

	iteration = iteration+1
	recursive(sentence2)	

	iteration = iteration - 2

		for i in  range(0, len(myConditions[iteration-1]))
			for j in range(0, len(myConditions[iteration-2]))
				disjuntion(myConditions[iteration-1][i], myConditions[iteration-2][j])

	
	return
	

def conjunction(sentence1, sentence2):
	recursive(sentence1)
	recursive(sentence2)
	return 

def negation(sentence):
	if neg_atom(sentence,0)
		myConditions[iteration].append(sentence[1])

	elif sentence[0]=='or'
		conjunction(('not', sentence1), ('not', sentence2))

	elif sentence[0]=='and' 
		disjunction(('not', sentence1), ('not', sentence2))

	elif sentence[0]=='<=>' 
		conjunction(sentence1, ('not', sentence2))
		conjunction(sentence2, ('not', sentence1))

	elif sentence[0]=='=>' 
		conjunction(sentence1, ('not', sentence2))


	return










	
	
