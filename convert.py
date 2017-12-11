# Program to convert logical sentences in propositional logic into CNF


import sys
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um


def recursive(line, myC):

	myConditions[iteration]=myC

	if line[0]=='<=>' :
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
	else:
		return True

	return


def atom(sentence):
	a = sentence[0] 
	if a =='<=>' or a == '=>' or a == 'or' or a == 'and' or a== 'not':
		return False
	else:
		return True
	return

def neg_atom(sentence):
	if sentence[0]=='not' and atom(sentence[1]):
		return True
	else:
		return False
	return

def literal(sentence):
	if (atom(sentence) or neg_atom(sentence)):
		print('literal')
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
	global iteration
	print('disj')
	if (atom(sentence1) and neg_atom(sentence2) and sentence2[1]==sentence1[0]) or (atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[0]):
		# disjunction of A and not A -> remove condition
		removing = (cond,sentence1,sentence2)
		myConditions[iteration].remove(set(removing))
		return
	if (atom(sentence1) and atom(sentence2) and sentence2[1]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[0]):
		# condition repeated -> remove one of them
		removing = (cond,sentence1,sentence2)
		myConditions[iteration].remove(set(removing))
		myConditions[iteration].append(set(sentence1))	
		return
	else:	
		removing = (cond,sentence1,sentence2)
		myConditions[iteration].remove(set(removing))
		appending = (sentence1, sentence2)
		myConditions[iteration].append(set(appending))


	return


def conjunction(cond, sentence1, sentence2):
	global iteration

	if sentence1 == sentence2:
		# two equal conjunctions
		removing = (cond,sentence1,sentence2)
		myConditions[iteration].remove(set(removing))
		myConditions[iteration].append(set(sentence1))

	else:
		removing = (cond,sentence1,sentence2)
		myConditions[iteration].remove(set(removing))
		myConditions[iteration+1]= myConditions[iteration]
		myConditions[iteration].append(set(sentence1))
		myConditions[iteration+1].append(set(sentence2))
		iteration=iteration+1
	return

def negation(cond, sentence):
	global iteration

	if sentence[0]=='not':
		removing = (cond,sentence)
		myConditions[iteration].remove(set(removing))
		appending = (sentence[1])
		myConditions[iteration].append(set(appending))
		return True

	elif sentence[0]=='or':
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

	j=0
	while (j==0):
		for i in range(0, len(myConditions)):
			print('here')
			j=0
			x = myConditions[i]
			while(j==0):
				for aux in range(0, len(x)):
					j=1
					if literal(x[aux]):
						myfinalConditions.append(set(x[aux]))
						print('here1')
						if x[aux][0] == 'or':
							print('mau')
						print(x[aux])
					else :
						recursive(x[aux],x)
						print(x[aux])
						print('not literal')
						j=0

print(myfinalConditions)


				


	

