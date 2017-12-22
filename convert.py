# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

def convert(sentence):

	equivalence(sentence)
	implication(sentence)
	negation(sentence)
	disjunction(sentence)
	switch_associative(sentence)
	disjunction(sentence)
	switch_associative(sentence)

def atom(sentence):
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		a = sentence[0]
		if (a == '<=>') or (a == '=>') or (a == 'or') or (a == 'and') or (a == 'not'):
			return False
		else:
			return True
	else:
		return False


def neg_atom(sentence):
	if len(sentence) > 2:
		return False
	elif len(sentence) == 2 and sentence[0] == 'not' and atom(sentence[1]):
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

	for cond in sentence:
		if len(cond)>1:
			equivalence(cond)


def implication(sentence):
	if(sentence[0] == '=>'):
		if len(sentence[1]) == 1:
			aux = ('not', sentence[1])
		else:
			aux = ['not', sentence[1]]
		sentence[0] = 'or'
		sentence[1] = aux

	for cond in sentence:
		if len(cond)>1:
			implication(cond)


def negation(sentence):
	if(sentence[0] == 'not'):
		if not neg_atom(sentence):
			aux = sentence[1]
			if aux[0] == 'not':
				sentence.remove('not')
				sentence[0] = sentence[0][1]

			elif aux[0] == 'or':
				sentence0 = 'and'
				if (aux[1][0]=='not'):
					sentence1 = aux[1][1]
				else:
					if len(aux[1]) == 1:
						sentence1 = ('not', aux[1])
					else:
						sentence1 = ['not', aux[1]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
				else:
					if len(aux[2]) == 1:
						sentence2 = ('not', aux[2])
					else:
						sentence2 = ['not', aux[2]]

				sentence[0]='and'
				sentence[1]=sentence1
				sentence.append(sentence2)

			elif aux[0]=='and':
				if (aux[1][0]=='not'):
					sentence1 = aux[1][1]
				else:
					if len(aux[1]) == 1:
						sentence1 = ('not', aux[1])
					else:
						sentence1 = ['not', aux[1]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
				else:
					if len(aux[2]) == 1:
						sentence2 = ('not', aux[2])
					else:
						sentence2 = ['not', aux[2]]

				sentence[0]='or'
				sentence[1]=sentence1
				sentence.append(sentence2)

	for cond in sentence[1:]:
		if len(cond)>1:
			negation(cond)



def disjunction(sentence):
	if(sentence[0] == 'or'):

		if (len(sentence[2])>1 and sentence[2][0] == 'and'):
				new1 = ['or', sentence[2][1], sentence[1]]
				new2 = ['or', sentence[2][2], sentence[1]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

		elif (len(sentence[1])>1 and sentence[1][0] =='and'):
				new1 = ['or', sentence[1][1], sentence[2]]
				new2 = ['or', sentence[1][2], sentence[2]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2

	for cond in sentence[1:]:
		if len(cond)>1:
			disjunction(cond)

def switch_associative(sentence):
	if(sentence[0] == 'and'):
		if (not literal(sentence[2]) and (sentence[2][0] == 'and')):
			if (literal(sentence[1]) or (sentence[1][0] == 'or')):
				aux1 = sentence[1]
				aux2 = sentence[2]
				sentence[2] = aux1
				sentence[1] = aux2


	for cond in sentence[1:]:
		if len(cond)>1:
			switch_associative(cond)


def dprint(sentence):
	if atom(sentence):
		s = [ '' if x == '[' else '' if x == ']' else x for x in repr(sentence)]
		sentence = eval("".join(s))

	if neg_atom(sentence):
		s = [ '(' if x == '[' else ')' if x == ']' else x for x in repr(sentence)]
		sentence = eval("".join(s))

	if sentence[0] == 'and':
		dprint(sentence[1])
		print(']', end='')
		print('')
		print('[', end='')
		dprint(sentence[2])
	elif sentence[0] == 'or':
		dprint(sentence[1])
		print(', ', end='')
		dprint(sentence[2])
	else:
		if len(sentence) == 1:
			print("'", end='')
			print(sentence, end='')
			print("'", end='')
		else:
			print(sentence, end='')

""" ------ MAIN FUNCTION ------ """


for line in sys.stdin:
	l = list(line)
	s = ['[' if x == '(' else ']' if x == ')' else x for x in l]
	new_line = "".join(s)

	sentence= list(eval(new_line))
	convert(sentence)

	print('[', end='')
	dprint(sentence)
	print(']')


