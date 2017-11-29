# Program to convert logical sentences in propositional logic into CNF


import sys
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um


def recursive(line, myConditions):
	
	if atom (line):
		return True

	elif line[0]=='<=>' :
		equivalence(line[0],line[1],line[2])

	elif line[0]== '=>' :
		implication(line[0],line[1],line[2])
		print(line)

	elif line[0]=='or' :
		disjunction(line[0],line[1],line[2])

	elif line[0]=='and' :
		conjunction(line[0],line[1],line[2])

	elif line[0]=='not' :
		if neg_atom(line):
			return True
		elif negation(line[0],line[1]):
			pass

	return


def atom(sentence):
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		return True
	return

def neg_atom(sentence):
	if len(sentence)==2 and sentence[0]=='not' and atom(sentence[1],0):
		return True
	else:
		return False
	return

def literal(sentence):
	if atom(sentence) or neg_atom(sentence):
		return True
	else:
		return False
	return

def equivalence(cond, sentence1, sentence2):
	implication(cond, sentence1,sentence2)
	implication(cond, sentence2,sentence1)
	return

def implication(cond, sentence1, sentence2):
	new = ('not', sentence1)
	disjunction(cond, new, sentence2)
	return

def disjunction(cond, sentence1, sentence2):
	if (atom(sentence1) and neg_atom(sentence2) and sentence2[1]==sentence1[0]) or (atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[0]):
		# disjunction of A and not A -> delete condition
		myConditions[iteration].delete(cond)
		myConditions[iteration].delete(sentence1)
		myConditions[iteration].delete(sentence2)			
		return
	if (atom(sentence1) and atom(sentence2) and sentence2[1]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[0]):
		# condition repeated -> remove one of them
		myConditions[iteration].delete(cond)
		myConditions[iteration].delete(sentence2)	
		return
	else:	
		myConditions[iteration].delete(cond)
		myConditions[iteration].append(sentence1)
		myConditions[iteration].append(sentence2)

	return


def conjunction(cond, sentence1, sentence2):
	if sentence1 == sentence2:
		# to equal conjunctions
		myConditions[iteration].delete(cond)
		myConditions[iteration].delete(sentence2)

	else:
		myConditions[iteration].delete(cond)
		myConditions[iteration+1]= myConditions[iteration]
		myConditions[iteration].delete(sentence1)
		myConditions[iteration+1].delete(sentence2)
		iteration=iteration+1
	return

def negation(cond, sentence):

	if sentence[0]=='or':
		new1 = ('not', sentence1)
		new2 = ('not', sentence2)
		conjunction('and',new1, new2)

	elif sentence[0]=='and':
		new1 = ('not', sentence1)
		new2 = ('not', sentence2)
		disjunction('or', new1, new2)

	elif sentence[0]=='<=>' :
		new1 = ('not', sentence1)
		new2 = ('not', sentence2)
		conjunction('and', sentence1, new1)
		conjunction('and', sentence2, new2)

	elif sentence[0]=='=>' :
		new2 = ('not', sentence2)
		conjunction('and', sentence1, new2)

	return



myfinalConditions = list()
myfinalConditions.append(list())


for line in sys.stdin:
	sentence = eval(line)
	global iteration
	iteration = 0
	myConditions = list()
	myConditions.append(list())
	myConditions[iteration].append(sentence)

	j=1

	recursive(x, myConditions)
	for a in range(0, len(myConditions[iteration])):
		print(d)
		if not literal(a):
			print(test)
			j=0

	if (j==0):
		(for i in range(0, iteration)):
			print(a)
			j=0
			while (j==0):
				print(b)
				for x in range(0, len(myConditions[i])):
					print(c)
					recursive(x, myConditions[i])
				j=1
				for a in range(0, len(myConditions[i])):
					print(d)
					if not literal(a):
						print(test)
						j=0

				


	myfinalConditions.append(myConditions)

		
	print(myfinalConditions[0])

