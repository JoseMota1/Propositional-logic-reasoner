# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def convert(sentence, myConditions):

	equivalence(sentence)

	implication(sentence)

	negation(sentence)

	disjunction(sentence)
	
	print('5', sentence)

	print('what')

	test = True 
	aux_not = False
	while test:
		aux_a = 0
		aux_o = 0
		test = False
		for cond in sentence:
			if len(cond)>1:
				if cond == 'and':
					aux_a = aux_a + 1
					aux_not = False
					test = True

				elif cond == 'or':
					aux_o = aux_o+1
					aux_not = False
					test = True

				elif cond == 'not':
					aux_not = cond

				elif aux_o > 0:
					if cond != 'and' or cond != 'or' or cond !='not':
						if aux_not != False:
							myConditions.extend((aux_not+cond))
						else:
							myConditions.extend(cond)	 
						aux_not = False
						aux_o = aux_o-1

				elif aux_a == 1:
					if cond != 'and' or cond != 'or' or cond !='not':
						a=list(myConditions)
						if aux_not != False:
							a.extend((aux_not+cond))
						else:
							a.extend(cond)
						aux_not = False
						aux_a = aux_a + 1 

				elif aux_a == 2:
					if cond != 'and' or cond != 'or' or cond !='not':
						b=list(myConditions)
						if aux_not != False:
							b.extend(aux_not)
						else:
							b.extend(cond)
						myConditions.clear()
						myConditions.extend(a + b)
						aux_not = False
						aux_a = 0

				else:
					myConditions.extend(cond)

				print('myC dntro ciclo', myConditions)

		aux = list()
		aux = copy.copy(sentence)
		sentence = list()
		sentence = copy.copy(myConditions)
		print('fim do for',sentence, 'test', test)
		myConditions = list()

	myConditions = copy.copy(aux)
	print('im true', aux)
			


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
	if(sentence[0] == '=>'):
		aux=['not', sentence[1]]
		sentence[0] = 'or'
		sentence[1] = aux	

	for cond in sentence[1:]:
		if len(cond)>1:
			implication(cond)

def negation(sentence):
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
		if len(cond)>1:
			disjunction(cond)


  


""" ------ MAIN FUNCTION ------ """

nlines = 0
myConditions=list()
for line in sys.stdin:
	l = list(line)
	s = ['[' if x == '(' else ']' if x == ')' else x for x in l]
	new_line = "".join(s)

	sentence= list(eval(new_line))
	convert(sentence, myConditions)

	nlines = nlines + 1



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
