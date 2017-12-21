# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def recursive(s, myConditions):

	print('1', s)
	equivalence(s)

	print('2', s)
	implication(s)

	print('3', s)
	negation(s)

	print('4', s)
	disjunction(s)
	
	print('5', s)


	a = 0
	o = 0
	for cond in sentence:
		if cond=='and':
			a = a + 1

		elif cond=='or':
			o = o + 1

		elif o == 1:
			or1 = cond
			o = o + 1 

		elif o == 2:
			or2 = cond
			myConditions.extend(or1)
			myConditions.extend(or2)
			o = 0

		elif a == 1:
			a1 = cond
			a = a + 1 

		elif a == 2:
			a2 = cond
			a=list(myConditions)
			b=list(myConditions)
			a.extend(a1)
			b.extend(a2)
			myConditions.clear()
			myConditions.extend(a + b)
			a = 0

		else:
			myConditions.extend(sentence)



			


def atom(sentence):
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		a = sentence[0]
		if (a =='<=>') or (a == '=>') or (a == 'or') or (a == 'and') or (a == 'not'):
			return False
		else:
			print('IS ATOM',sentence)
			return True
	else:
		return False



def neg_atom(sentence):
	if len(sentence) > 2:
		return False
	elif len(sentence) == 2 and sentence[0] == 'not' and atom(sentence[1]):
		print('NEGATOM',sentence)
		return True
	else:
		return False


def literal(sentence):
	if (atom(sentence) or neg_atom(sentence)):
		return True
	else:
		return False


def equivalence(sentence):
	if(sentence[0] == '<=>'):
		aux1 = sentence[1]
		aux2 = sentence[2]
		sentence[0] = 'and'
		sentence[1] = ['=>', aux1, aux2]
		sentence[2] = ['=>', aux2, aux1]

	for cond in sentence[1:]:
		if len(cond)>1:
			equivalence(cond)

def implication(sentence):
	print('HEEEEEEEE',sentence)
	if(sentence[0] == '=>'):
		aux=['not', sentence[1]]
		sentence[0] = 'or'
		sentence[1] = aux	

	for cond in sentence[1:]:
		if len(cond)>1:
			implication(cond)

def negation(sentence):
	print('negation',sentence)
	if(sentence[0] == 'not'):
		print('entered', sentence)
		if not neg_atom(sentence):
			print('sentencemerda' , sentence[1])
			aux = sentence[1]
			print('here', aux[0])
			if aux[0] == 'not':
				print('i am here', sentence[1][1])
				sentence.remove('not')
				sentence[0] = sentence[0][1]

			elif aux[0] == 'or':		
				sentence0 = 'and'
				if (aux[1][0]=='not'):
					sentence1 = aux[1][1]
				else:
					sentence1 = ['not', [aux[1]]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
				else:
					sentence2 = ['not', [aux[2]]]

				sentence[0]='and'
				sentence[1]=sentence1
				sentence.append(sentence2)

			elif aux[0]=='and':
				if (aux[1][0]=='not'):
					sentence1 = aux[1][1]
				else:
					sentence1 = ['not', [aux[1]]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
				else:
					sentence2 = ['not', [aux[2]]]

				sentence[0]='or'
				sentence[1]=sentence1
				sentence.append(sentence2)
	
	for cond in sentence[1:]:
		if len(cond)>1:
			negation(cond)
		


def disjunction(sentence):
	if(sentence[0] == 'or'):
		if (literal(sentence[1]) and literal(sentence[2])):
			return

		elif (literal(sentence[1])):
			new1 = ['or', sentence[1], sentence[2][1]]
			new2 = ['or', sentence[1], sentence[2][2]]

			if sentence[2][0] == 'and':
				sentence[0] = 'and'
			elif sentence[2][0] == 'or':
				sentence[0] = 'or'

			sentence[1] = new1
			sentence[2] = new2


		elif (literal(sentence[2])):
			new1 = ['or', sentence[2], sentence[1][1]]
			new2 = ['or', sentence[2], sentence[1][2]]

			if sentence[1][0]=='and':
				sentence[0] = 'and'
			elif sentence[1][0]=='or':
				sentence[0] = 'or'

			sentence[1] = new1
			sentence[2] = new2

		elif sentence[1][0] =='and':
			if sentence[2][0] == 'or':
				new1 = ['or', sentence[1][1], sentence[2]]
				new2 = ['or', sentence[1][2], sentence[2]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

			elif sentence2[0] == 'and':
				new1=['or', sentence[1][1], sentence[2][1]]
				new2=['or', sentence[1][2], sentence[2][1]]
				new3=['or', sentence[1][1], sentence[2][2]]
				new4=['or', sentence[1][2], sentence[2][2]]
				sentence1=['and',new1, new2]
				sentence2=['and', new3, new4]
				sentence[0] = 'and'
				sentence[1] = sentence1
				sentence[2] = sentence2

		elif sentence1[0]=='or':
			if sentence2[0]== 'and':
				new1 = ['or', sentence[2][1], sentence[1]]
				new2 = ['or', sentence[2][2], sentence[1]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

	
	for cond in sentence[1:]:	
		if not literal(cond):
			disjunction(cond)


  





  


nlines = 0
myConditions=list()
for line in sys.stdin:
	l = list(line)
	s = ['[' if x == '(' else ']' if x == ')' else x for x in l]
	new_line = "".join(s)

	sentence= list(eval(new_line))
	recursive(sentence, myConditions)


	nlines = nlines + 1

#print('myFinalConditions', myFinalConditions)

# print(nconjuntions)
# if nconjuntions:
# 	myFinalConditions = myFinalConditions[0]

# print(myFinalConditions, '\n Solution:')
print(nlines > 1)
for condition in myConditions:
	if nlines > 1:
		print(condition)
	else:
		if condition:
			if not isinstance(condition[0], list):
				print(condition)
			else:
				for e in condition:
					print(e)
