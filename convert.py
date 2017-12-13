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
		else:
			negation(line[0],line[1], myConditions)
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

	conjunction('and', new1, new2, myConditions)

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
	print('disj', sentence1, sentence2, myConditions)


	if (atom(sentence1) and atom(sentence2) and sentence2[0]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[1]):
	# condition repeated -> remove one of them
		myConditions.append(sentence1)
		return

	else:
		if literal(sentence1):
			myConditions.append(sentence1)

		if literal(sentence2):
			myConditions.append(sentence2)

		if not literal(sentence1):
			recursive(sentence1, myConditions)

		if not literal(sentence2):
			recursive(sentence2, myConditions)
			return

		return


def conjunction(cond, sentence1, sentence2, myConditions):
	print('conj', myConditions)

	if( literal(sentence1) and literal(sentence2) ):
		if sentence1 == sentence2:
			# two equal conjunctions
			myConditions.append(sentence1)
			return

		if  neg_atom(sentence1) and atom(sentence2):
			if sentence2 == sentence1[1]:
				return

		if  neg_atom(sentence2) and atom(sentence1):
			if sentence1 == sentence2[1]:
				return

	a = list(myConditions)
	b = list(myConditions)

	print('s1', sentence1, 's2', sentence2)
	print('conj2 b4', myConditions)

	print('a b4', a)
	print('b b4', b)

	recursive(sentence1, a)
	recursive(sentence2, b)

	del myConditions[:]
	myConditions.append(a)
	myConditions.append(b)

	print('a after', a)
	print('b after', b)

	print('conj2 after', myConditions)


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

	elif sentence[0]=='or':
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		conjunction('and',new1, new2, myConditions)


	elif sentence[0]=='and':
		new1 = ('not', sentence[1])
		new2 = ('not', sentence[2])
		disjunction('or', new1, new2, myConditions)


	elif sentence[0]=='<=>' :
		new1 = ('=>', sentence[1], sentence[2])
		new2 = ('=>', sentence[2], sentence[1])
		negation('not', new1, myConditions)
		negation('not', new2, myConditions)



	elif sentence[0]=='=>' :
		new = ('not', sentence[2])
		new2 = ('and', sentence[1], new)
		recursive(new2, myConditions)
	return



myfinalConditions = list()
myConditionsaux = list()
for line in sys.stdin:
	sentence = eval(line)
	recursive(sentence, myConditionsaux)
	myfinalConditions.append(copy.copy(myConditionsaux))
	myConditionsaux.clear()

print('myfinalConditions', myfinalConditions)

print(len(myfinalConditions[0]))
"""for e in myfinalConditions:
	while len(e) == 1:
		if len(e[0] == 1):
			e = e[0]
		else:
			for i in e:
				print (i)"""
