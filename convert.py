# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def recursive(line, myConditions):
	print('recursive', myConditions)

	if line[0] == '<=>' :
		equivalence(line[0],line[1],line[2], myConditions)

	elif line[0] == '=>' :
		implication(line[0],line[1],line[2], myConditions)

	elif line[0] == 'or' :
		disjunction(line[0],line[1],line[2], myConditions)

	elif line[0] == 'and' :
		conjunction(line[0],line[1],line[2], myConditions)

	elif line[0] == 'not' :
		if neg_atom(line):
			myConditions.append(line)

		else:
			negation(line[0],line[1], myConditions)
	else:
		global isConjunction
		if isConjunction:
			if len(myConditions) > 1:
				for condition in myConditions:
					condition.append(line)
			else:
				myConditions.append(line)
			isConjunction = False
		else:
			myConditions.append(line)



def atom(sentence):
	a = sentence[0]
	if a =='<=>' or a == '=>' or a == 'or' or a == 'and' or a== 'not':
		return False
	else:
		return True


def neg_atom(sentence):
	if sentence[0]=='not' and atom(sentence[1]):
		return True
	else:
		return False


def literal(sentence):
	if (atom(sentence) or neg_atom(sentence)):
		return True
	else:
		return False


def equivalence(cond, sentence1, sentence2, myConditions):
	print('equivalence', myConditions)
	new1 = ('=>', sentence1,sentence2)
	new2 = ('=>', sentence2,sentence1)

	conjunction('and', new1, new2, myConditions)

def implication(cond, sentence1, sentence2, myConditions):
	print('implication', myConditions)

	if sentence1[0] == 'not':
		new = sentence1[1]
	else:
		new = ('not', sentence1)

	disjunction('or', new, sentence2, myConditions)


def disjunction(cond, sentence1, sentence2, myConditions):
	print('disjunction', myConditions)

	if (atom(sentence1) and atom(sentence2) and sentence2[0]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[1]):
	# condition repeated -> remove one of them
		myConditions.append(sentence1)

	else:
		if literal(sentence1):
			if len(myConditions) > 1:
				for condition in myConditions:
					condition.append(sentence1)
			else:
				myConditions.append(sentence1)

		if literal(sentence2):
			if len(myConditions) > 1:
				for condition in myConditions:
					condition.append(sentence2)
			else:
				myConditions.append(sentence2)

		if not literal(sentence1):
			recursive(sentence1, myConditions)

		if not literal(sentence2):
			recursive(sentence2, myConditions)


def conjunction(cond, sentence1, sentence2, myConditions):
	print('conjunction', myConditions)

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

	print('a before', a)
	print('b before', b)

	global isConjunction
	isConjunction = True
	recursive(sentence1, a)
	isConjunction = True
	recursive(sentence2, b)

	print('a after', a)
	print('b after', b)

	print('myConditions before clear', myConditions)
	myConditions.clear()
	print('myConditions afer clear', myConditions)
	# print('a.append(b)', a)
	if isinstance(a[0], list) and isinstance(b[0], list):
		myConditions.extend(a + b)
		print('myConditions.extend(a + b)', myConditions)
	elif isinstance(a[0], list):
		myConditions.extend(a + [b])
		print('myConditions.extend(a + [b])', myConditions)
	elif isinstance(b[0], list):
		myConditions.extend([a] + b)
		print('myConditions.extend([a] + b)', myConditions)
	else:
		myConditions.extend([a] + [b])
		print('myConditions.extend([a] + [b])', myConditions)
	# global nconjuntions
	# nconjuntions = nconjuntions + 1


	# print('conjunction after', myConditions)


def negation(cond, sentence, myConditions):
	print('negation', myConditions)

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


nlines = 0
myFinalConditions = list()
myConditionsAux = list()
for line in sys.stdin:
	sentence = eval(line)
	recursive(sentence, myConditionsAux)
	myFinalConditions.append(list(myConditionsAux))
	myConditionsAux.clear()
	nlines = nlines + 1

print('myFinalConditions', myFinalConditions)

# print(nconjuntions)
# if nconjuntions:
# 	myFinalConditions = myFinalConditions[0]

# print(myFinalConditions, '\n Solution:')
print(nlines > 1)
for condition in myFinalConditions:
	if nlines > 1:
		print(condition)
	else:
		if condition:
			if not isinstance(condition[0], list):
				print(condition)
			else:
				for e in condition:
					print(e)
