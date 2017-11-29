# Program to convert logical sentences in propositional logic into CNF


import sys
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

myConditions = list()
myConditions.append(list())

def recursive(line):
	print(line)
	if atom (line,True):
		pass

	elif line[0]=='<=>' :
		equivalence(line[1],line[2])

	elif line[0]== '=>' :
		implication(line[1],line[2])
		print(line)

	elif line[0]=='or' :
		disjunction(line[1],line[2])

	elif line[0]=='and' :
		conjunction(line[1],line[2])

	elif line[0]=='not' :
		if neg_atom(line,True):
			pass
		elif negation(line[1]):
			pass

	return


def atom(sentence, value):
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		if value == True:
			global iteration
			myConditions[iteration].append(sentence)
		return True
	return

def neg_atom(sentence, value):
	if len(sentence)==2 and sentence[0]=='not' and atom(sentence[1],0):
		if value == True:
			global iteration
			myConditions[iteration].append(sentence)
		return True
	else:
		return False
	return


def equivalence(sentence1, sentence2):
	implication(sentence1,sentence2)
	implication(sentence2,sentence1)
	return

def implication(sentence1, sentence2):
	new1 = ('not', sentence1)
	disjunction(new1, sentence2);
	return

def disjunction(sentence1, sentence2):
	if (atom(sentence1,0) or neg_atom(sentence1,0)) and (atom(sentence2,0) or neg_atom(sentence2,0)):
		if (atom(sentence1,0) and neg_atom(sentence2,0) and sentence2[1]==sentence1[0]) or (atom(sentence2,0) and neg_atom(sentence1,0) and sentence1[1]==sentence2[0]):# ignora-se.
			return
		if (atom(sentence1,0) and atom(sentence2,0) and sentence2[1]==sentence1[0]) or (neg_atom(sentence2,0) and neg_atom(sentence1,0) and sentence1[1]==sentence2[0]):# ignora-se.
			myConditions[iteration].append((sentence1))
			return
		else:	
			global iteration
			myConditions[iteration].append((sentence1, sentence2)) # not sure this is how its done
			print('disj')
	else:
		if not aux_dist(sentence1, sentence2):
			if not aux_dist(sentence2, sentence1):			
				if not aux2_dist(sentence1, sentence2):
					aux2_dist(sentence2, sentence1)
	return


def aux_dist(sentence1, sentence2):
	global iteration
	if (atom(sentence1,0) or neg_atom(sentence1,0)):
		if sentence2[0]=='or':
			if (atom(sentence2[1]) or neg_atom(sentence2[1])) && (atom(sentence2[2]) or neg_atom(sentence2[2])):
				myConditions[iteration].append((sentence1, sentence2[1], sentence[2]))
				return True
			else:
				aux2_dist(sentence2[1], sentence2[2])

		elif sentence2[0]=='and':
			disjunction(sentence1, sentence2[1])
			disjunction(sentence1, sentence2[2])
			return True

		elif sentence[0]=='<=>' :
			new1 = ('not', sentence2[1])
			new2 = ('not', sentence2[2])
			myConditions[iteration].append((sentence1, new1, sentence[2]))
			myConditions[iteration].append((sentence1, new2, sentence[1]))
			return True
		elif sentence[0]=='=>' :
			new1 = ('not', sentence2[1])
			myConditions[iteration].append((sentence1, new1, sentence[2]))
			return True

	return

def aux2_dist(sentence1, sentence2):
	global iteration
	if (atom(sentence1,0) or neg_atom(sentence1,0)):
		if sentence2[0]=='or':
			if (atom(sentence2[1]) or neg_atom(sentence2[1])) && (atom(sentence2[2]) or neg_atom(sentence2[2])):
				myConditions[iteration].append((sentence1, sentence2[1], sentence[2]))
				return True
			else:
				aux_dist(sentence2[1], sentence[2])

		elif sentence2[0]=='and':
			disjunction(sentence1, sentence2[1])
			disjunction(sentence1, sentence2[2])
			return True

		elif sentence[0]=='<=>' :
			new1 = ('not', sentence2[1])
			new2 = ('not', sentence2[2])
			myConditions[iteration].append((sentence1, new1, sentence[2]))
			myConditions[iteration].append((sentence1, new2, sentence[1]))
			return True
		elif sentence[0]=='=>' :
			new1 = ('not', sentence2[1])
			myConditions[iteration].append((sentence1, new1, sentence[2]))
			return True

	return




def conjunction(sentence1, sentence2):
	if (sentence1 == sentence2):
		recursive(sentence1)
	else:
		recursive(sentence1)
		recursive(sentence2)
	return

def negation(sentence):

	if neg_atom(sentence,0):
		global iteration
		myConditions[iteration].append(sentence[1])

	elif sentence[0]=='or':
		conjunction(('not', sentence1), ('not', sentence2))

	elif sentence[0]=='and':
		disjunction(('not', sentence1), ('not', sentence2))

	elif sentence[0]=='<=>' :
		conjunction(sentence1, ('not', sentence2))
		conjunction(sentence2, ('not', sentence1))

	elif sentence[0]=='=>' :
		conjunction(sentence1, ('not', sentence2))

	return



for lines in sys.stdin:
	sentences = eval(lines)
	global iteration
	iteration = 0
	recursive(sentences)
	print(myConditions[0])

