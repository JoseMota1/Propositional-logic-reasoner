# Program to convert logical sentences in propositional logic into CNF


import sys
import copy
#Vai ler do pipe cada coisa introduzida  e diferenciar cada um

isConjunction = False

def convert(sentence):

	print('original:', sentence, 'end')
	equivalence(sentence)
	print('equivalence:', sentence, 'end')
	implication(sentence)
	print('implication:', sentence, 'end')
	negation(sentence)
	print('negation:', sentence, 'end')
	disjunction(sentence)
	print('disjunction', sentence, 'end')
	#finishing_or(sentence)
	#print('or_finish', sentence, 'end')
	#finishing_and(sentence)
	#print('and_finish', sentence, 'end')


def atom(sentence):
	if len(sentence)>1:
		return False
	elif len(sentence)==1:
		a = sentence[0]
		if (a =='<=>') or (a == '=>') or (a == 'or') or (a == 'and') or (a == 'not'):
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
					sentence1 = ['not', aux[1]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
				else:
					sentence2 = ['not', aux[2]]

				sentence[0]='and'
				sentence[1]=sentence1
				sentence.append(sentence2)

			elif aux[0]=='and':
				if (aux[1][0]=='not'):
					sentence1 = aux[1][1]
				else:
					sentence1 = ['not', aux[1]]
				if (aux[2][0] == 'not'):
					sentence2 = aux[2][1]
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

			elif sentence[2][0] == 'and':
				new1=['or', sentence[1][1], sentence[2][1]]
				new2=['or', sentence[1][2], sentence[2][1]]
				new3=['or', sentence[1][1], sentence[2][2]]
				new4=['or', sentence[1][2], sentence[2][2]]
				sentence1=['and',new1, new2]
				sentence2=['and', new3, new4]
				sentence[0] = 'and'
				sentence[1] = sentence1
				sentence[2] = sentence2

		elif sentence[1][0]=='or':
			if sentence[2][0]== 'and':
				new1 = ['or', sentence[2][1], sentence[1]]
				new2 = ['or', sentence[2][2], sentence[1]]
				sentence[0] = 'and'
				sentence[1] = new1
				sentence[2] = new2


	for cond in sentence[1:]:
		if len(cond)>1:
			disjunction(cond)


def finishing_or(sentence):
	if sentence[0] == 'or':
		#print('1111', sentence[1])
		#print('1222', sentence[2])
		aux0 = sentence[1]
		aux1 = sentence[2]

		sentence.remove('or')
		sentence.remove(aux0)
		sentence.remove(aux1)

		sentence.append(aux0)


		sentence.append(aux1)


	for cond in sentence[1:]:
		if len(cond)>1:
			finishing_or(cond)

def finishing_and(sentence):
	if sentence[0] == 'and':
		#print('2111', sentence[1])
		#print('2222', sentence[2])
		aux0=sentence[1]
		aux1=sentence[2]
		sentence.remove('and')
		sentence.remove(aux0)
		sentence.remove(aux1)
		sentence.append(aux0)
		sentence.append(aux1)


	for cond in sentence[1:]:
		if len(cond)>1:
			finishing_and(cond)

#def fix_sentences(sentence):








""" ------ MAIN FUNCTION ------ """

nlines = 0
myConditions=list()
for line in sys.stdin:
	l = list(line)
	s = ['[' if x == '(' else ']' if x == ')' else x for x in l]
	new_line = "".join(s)

	sentence= list(eval(new_line))
	convert(sentence)

	print(sentence)
	nlines = nlines + 1

"""	for condition in sentence:
		if literal(sentence):
			condition = sentence
		if (nlines > 1 and (not literal(sentence))):
			print(condition)
		else:
			if condition:
				if not isinstance(condition[0], list):
					l = repr(condition)
					s = ['' if (x == '(') or (x == ')') or (x == '[') or (x == ']') else x for x in l]
					new_cond = "".join(s)
					new_cond = '[' + new_cond
					new_cond = new_cond + ']'
					s = new_cond
					fw = 0
					for i in range(len(new_cond) - 4):
						if (new_cond[i] == "'" and new_cond[i+1] == 'n' and new_cond[i+2] == 'o' and
								new_cond[i+3] == 't' and new_cond[i+4] == "'"):
							pp = 0
							pi = 0
							for c in s[(i+fw):]:
								pi += 1
								if c == "'":
									pp += 1
								if(pp) == 4:
									break

							s = s[:(i+fw)] + '(' + s[(i+fw):(i+pi+fw)] + ')' + s[(i+pi+fw):]
							fw += 2
					print(s)
				else:
					for e in condition:
						l = repr(e)
						s = ['' if (x == '(') or (x == ')') or (x == '[') or (x == ']') else x for x in l]
						new_cond = "".join(s)
						new_cond = '[' + new_cond
						new_cond = new_cond + ']'
						s = new_cond
						fw = 0
						for i in range(len(new_cond) - 4):
							if (new_cond[i] == "'" and new_cond[i+1] == 'n' and new_cond[i+2] == 'o' and
									new_cond[i+3] == 't' and new_cond[i+4] == "'"):
								pp = 0
								pi = 0
								for c in s[(i+fw):]:
									pi += 1
									if c == "'":
										pp += 1
									if(pp) == 4:
										break

								s = s[:(i+fw)] + '(' + s[(i+fw):(i+pi+fw)] + ')' + s[(i+pi+fw):]
								fw += 2
						print(s)"""
