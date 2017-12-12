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

	print('equi1', myConditions)

	a=list(copy.deepcopy(myConditions))
	b=list(copy.deepcopy(myConditions))

	del myConditions[:]

	myConditions.append([a]+[b])

	recursive(new1, a)
	recursive(new2, b)
	print('HHHHHH', a)
	print('HHHHHH', b)
	print('this is ' , myConditions)

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


	if (atom(sentence1) and atom(sentence2) and sentence2[0]==sentence1[0]) or (neg_atom(sentence2) and neg_atom(sentence1) and sentence1[1]==sentence2[1]):
	# condition repeated -> remove one of them
		myConditions.append(sentence1)	
		return

	else:

		print('disj1', myConditions)	
		if literal(sentence1):
			myConditions.append(sentence1)
			print('hhhhh')
		
		if not literal(sentence1):
			recursive(sentence1, myConditions)
			print('hhhhh2')

		if literal(sentence2):
			myConditions.append(sentence2)
			print('hhhhh3')
			return

		if not literal(sentence2):	
			recursive(sentence2, myConditions)
			print('hhhhh4')
			return

		print('disj2', myConditions)	
		return


def conjunction(cond, sentence1, sentence2, myConditions):
	print('conj', myConditions)

	aux = 0
	if( literal(sentence1) and literal(sentence2) ):
		print('conjliteral')
		if sentence1 == sentence2:
			# two equal conjunctions
			myConditions.append(sentence1)
			aux=1
			return

		if  neg_atom(sentence1) and atom(sentence2):
			if sentence2 == sentence1[1]:
				aux=1
				return 
				
		if  neg_atom(sentence2) and atom(sentence1):
			if sentence1 == sentence2[1]:
				aux=1
				return 
	
	if (aux==0):	
		print('conj not literal')

		aa=list(copy.deepcopy(myConditions))
		bb=list(copy.deepcopy(myConditions))
		del myConditions[:]

		myConditions.append([aa] + [bb])

		if literal(sentence1):
			aa.append(sentence1)

		elif not literal(sentence1):
			recursive(sentence1, aa)

		if literal(sentence2):
			bb.append(sentence2)

		elif not literal(sentence2):			
			recursive(sentence2, bb)





		print('IIIII', aa)
		print('IIIIIII', bb)

		print('conj2', myConditions)

	

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
		new1 = ('or', n1, sentence[1])
		new2 = ('or', n2, sentence[2])
		new3 = ('or', sentence[1],sentence[2])


		aaa=list(copy.deepcopy(myConditions))
		bbb=list(copy.deepcopy(myConditions))
		ccc=list(copy.deepcopy(myConditions))
		del myConditions[:]

		recursive(new1, aaa)
		recursive(new2, bbb)
		recursive(new3, ccc)
		barra_n = list('\n')

		myConditions.append(aaa + bbb + ccc)
		print('KJJJJJJ', aaa)
		print('KJJJJJJ', bbb)
		print('KJJJJJJ', ccc)

		print('conj2', myConditions)


	elif sentence[0]=='=>' :
		new = ('not', sentence[2])
		new2 = ('and', sentence[1], new)
		print('not-imp', myConditions)
		recursive(new2, myConditions)
	return



myfinalConditions = list()
myConditionsaux = list()
for line in sys.stdin:
	sentence = eval(line)
	recursive(sentence, myConditionsaux)
	myfinalConditions.append(copy.copy(myConditionsaux))
	myConditionsaux.clear()

print('final2', myfinalConditions)



	

