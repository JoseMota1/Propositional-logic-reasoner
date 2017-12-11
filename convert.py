# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um


def recursive(line, myConditions):

	if line[0]=='<=>' :
		equivalence(line[0],line[1],line[2], myConditions)

	elif line[0]== '=>' :
		implication(line[0],line[1],line[2], myConditions)

	elif line[0]=='or' :
		disjunction(line[0],line[1],line[2], myConditions)

	elif line[0]=='and' :
		conjunction(line[0],line[1],line[2], myConditions)

	elif line[0]=='not' :
		if neg_atom(line):
			myConditions.append(line)
			return True
		elif negation(line[0],line[1], myConditions):
			pass
	else:
		myConditions.append(line)
		return True


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
		return True
	else:
		return False
	return

def equivalence(cond, sentence1, sentence2, myConditions):
	new1 = ('=>', sentence1,sentence2)
	new2 = ('=>', sentence2,sentence1)

	print('equi1', myConditions)

	a=copy.copy(myConditions)
	b=copy.copy(myConditions)
	del myConditions[:]
	recursive(new1, a)
	recursive(new2, b)

	myConditions.append(a)
	myConditions.append(b)



	print('equi2', myConditions)

	return

def implication(cond, sentence1, sentence2, myConditions):
	print('imp' , myConditions)

	if sentence1[0] == 'not':
		new = sentence1[1]
	else:
		new = ('not', sentence1)

	disjunction('or', new, sentence2, myConditions)

	return

def disjunction(cond, sentence1, sentence2, myConditions):
	print('disj', myConditions)

	if (atom(sentence1) and neg_atom(sentence2) and sentence2[1]==sentence1[0]) or (atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[0]):
	# disjunction of A and not A -> remove condition
		return

	elif (atom(sentence1) and atom(sentence2) and sentence2[0]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[1]):
	# condition repeated -> remove one of them
		myConditions.append(sentence1)	
		return

	else:
		if literal(sentence1):
			myConditions.append(sentence1)
		
		elif not literal(sentence1):
			recursive(sentence1, myConditions)

		if literal(sentence2):
			myConditions.append(sentence2)

		elif not literal(sentence2):	
			recursive(sentence2, myConditions)

		print('disj2', myConditions)	
		return


def conjunction(cond, sentence1, sentence2, myConditions):
	print('conj', myConditions)

	if( literal(sentence1) and literal(sentence2) ):
		if sentence1 == sentence2:
			# two equal conjunctions
			if literal(sentence1):
				myConditions.append(sentence1)
			else:
				recursive(sentence1, myConditions)
				return

		elif  sentence1[0] == 'not':
			print('1')
			if sentence2 == sentence1[1]:
				return

		elif  sentence2[0] == 'not':
			print('2')
			if sentence1 == sentence2[1]:
				return

	print('aaah')
	else:
		print('3')
		a=copy.copy(myConditions)
		b=copy.copy(myConditions)
		del myConditions[:]

		if literal(sentence1):
			a.append(sentence1)
		
		elif not literal(sentence1):
			recursive(sentence1, a)

		if literal(sentence2):
			b.append(sentence2)

		elif not literal(sentence2):			
			recursive(sentence2, b)

		myConditions.append(a)
		myConditions.append(b)
		print('conj2', myConditions)

		return

def negation(cond, sentence, myConditions):
	print('neg', myConditions)

	if atom(sentence):
		new = ('not', sentence)
		myConditions.append(new)

	elif sentence[0]=='not':
		if atom(sentence[1]):
			myConditions.append(sentence[1])
		else:
			recursive(sentence, myConditions)
		return True

	elif sentence[0]=='or':
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		print('not-or', sentence)
		conjunction('and',new1, new2, myConditions)


	elif sentence[0]=='and':
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		print('not-and', sentence)
		disjunction('or', new1, new2, myConditions)


	elif sentence[0]=='<=>' :
		n1 = ('not', sentence[1])
		n2 = ('not', sentence[2])
		new1 = ('and', sentence[1], new2)
		new2 = ('and', sentence[2], new1)
		print('not-equ', sentence)
		disjunction('or', new1, new2, myConditions)


	elif sentence[0]=='=>' :
		new2 = ('not', sentence[2])
		print('not-imp', sentence)
		conjunction('and', sentence[1], new2, myConditions)
	return




myfinalConditions = list()

for line in sys.stdin:
	sentence = eval(line)
	myConditions = list()
	recursive(sentence, myConditions)
	print('final', myConditions)
	myfinalConditions.append(myConditions)

print('HERE', myfinalConditions)


				


	

